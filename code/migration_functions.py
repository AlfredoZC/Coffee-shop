import connection

class Table:
    def __init__(self, name : str, columns : list, rows : list):
        self.name = name 
        self.columns = columns
        self.rows = rows
    def __str__(self):
        return f"Table (nombre = {self.name}, colums = {self.columns}, row = {self.rows})"    

def get_tables_mysql(cursor):
    cursor.execute("SHOW TABLES")
    return [row[0] for row in cursor.fetchall()]

def get_colums_mysql(cursor, tabla):
    cursor.execute(f"DESCRIBE {tabla}")
    return [ row[0] for row in cursor.fetchall()]

def get_data_mysql(cursor,tabla,columns):
    column_list = ', '.join(columns)
    cursor.execute(f"SELECT {column_list} FROM {tabla}")
    return cursor.fetchall()

def map_mysql_to_sqlserver(mysql_type):
# Mapea los tipos de datos de sql:
    mapping = {
        'int': 'INT',
        'tinyint':'SMALLINT',
        'varchar': 'NVARCHAR',
        'text':'NVARCHAR(MAX)',
        'date':'DATE',
        'datetime': 'DATETIME2',
        'decimal': 'DECIMAL',
        'float': 'FLOAT',
        'boolean': 'BIT',
    }
    
    for key in mapping:
        if key in mysql_type.lower(): # nos permite una comparacion parcial y no exacta como ==
            return mapping[key]
        return mysql_type #No esta mapeado.

def get_primary_key(table_name, mysql_cursor):
    mysql_cursor.execute(f"SHOW KEYS FROM {table_name} WHERE key_name = 'PRIMARY' ;")
    primary_key = [row[4] for row in mysql_cursor.fetchall()]
    return primary_key 

def create_table(mysql_cursor, sqlserver_cursor, table_name):

    try:
        mysql_cursor.execute(f"DESCRIBE `{table_name}`")
        columns = mysql_cursor.fetchall()
        if not columns:
            print(f"No se obtuvieron columnas para la tabla '{table_name}'.")
            return
    except Exception as e:
        print(f"Error al describir la tabla '{table_name}': {e}")
        return
    
    primary_key = get_primary_key(table_name, mysql_cursor)
    
    sqlserver_query = f"CREATE TABLE {table_name} ( \n" # Query que necesitaremos. para crear la tabla
    columndata = []  #Esta lista nos ayudara a guardar los datos para rellenar el query y crear la tabla
    for column in columns: 
        column_name = column[0]
        column_type = map_mysql_to_sqlserver(column[1])
        nullstuff = "NOT NULL" if column[2] == 'NO'  else "NULL" 
        extra = "IDENTITY(1,1)" if "auto_increment" in column[5].lower() else ""
        columndata.append(f"{column_name} {column_type} {nullstuff} {extra}")

    if primary_key:
        primary_key_new = ",".join(primary_key)
        columndata.append(f"PRIMARY KEY ({primary_key_new})")

    sqlserver_query += ",\n".join(columndata) + "\n);"
    print(sqlserver_query)
    print(f"Creando tabla: {table_name}")
    sqlserver_cursor.execute(sqlserver_query)
   

def migrate_mysql_to_sqlserver(mysql_config, sqlserver_config):
    try:
        #Conexion a mysql
        print("conectandose a mysql")
        mysql_connection =  connection.mysql_connection(mysql_config)
        mysql_cursor = mysql_connection.cursor()
        #Conexion a sqlserver
        print("conectandose a sqlserver")
        sqlserver_connection = connection.sqlserver_connection(sqlserver_config)
        sqlserver_cursor = sqlserver_connection.cursor()

        tables = [] # Esto almacenara objetos tipo Table
        
        #obtener el nombre de todas las tablas
        table_names = get_tables_mysql(mysql_cursor)
        for table_name in table_names:
            print(f"Cargando datos de la tabla{table_name}")
            create_table(mysql_cursor,sqlserver_cursor,table_name) # creamos las tablas en sqlserver 1x1
            sqlserver_connection.commit() #Hacemos un commit a las tablas creadas en sql server
            columnas = get_colums_mysql(mysql_cursor, table_name)
            filas = get_data_mysql(mysql_cursor, table_name, columnas)

            # Objeto tipo table:
            table = Table(name = table_name, columns = columnas, rows = filas)
            tables.append(table)
            
        #migrar datos
        for table in tables:
            if not isinstance(table, Table):
                 raise TypeError(f"Error: {table} no es una instancia válida de Table")
            else:
                print(f"Se esta migrando la tabla: {table.name}")
                columnas = table.columns 
                filas = table.rows

                column_list = ','.join(columnas)
                placeholders = ','.join(['?'] * len(columnas))
                insert_query = f"INSERT INTO {table.name} ({column_list}) VALUES ({placeholders})"

                for fila in filas:
                    try:
                        sqlserver_cursor.execute(f"SET IDENTITY_INSERT {table.name} ON")
                        sqlserver_cursor.execute(insert_query, fila)
                        sqlserver_cursor.execute(f"SET IDENTITY_INSERT {table.name} OFF")

                    except Exception as e:
                        print(f"Error al insertar los datos en {table_name}:" , e)

                sqlserver_connection.commit()

    except Exception as e:
        print(f"Error durante la migracion: {e}")


        if 'mysql_connection' in locals():
            mysql_connection.close()
        if 'sqlserver_connection' in locals():
            sqlserver_connection.close()










