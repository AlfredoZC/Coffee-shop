import libraries as lbs 
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

def migrate_mysql_to_sqlserver(mysql_config, sqlserver_config):
    try:
        #Conexion a mysql
        mysql_connection =  connection.mysql_connection(mysql_config)
        mysql_cursor = mysql_connection.cursor()

        sqlserver_connection = connection.sqlserver_connection(sqlserver_config)
        sqlserver_cursor = sqlserver_connection.cursor()

        tables = [] # Esto almacenara objetos tipo Table
        
        #obtener el nombre de todas las tablas
        table_names = get_tables_mysql(mysql_cursor)
        for table_name in table_names:
            print(f"Cargando datos de la tabla{table_name}")

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
                    sqlserver_cursor.execute(insert_query, fila)

            
                sqlserver_connection.commit()

    except Exception as e:
        print(f"Error durante la migracion: {e}")


        if 'mysql_connection' in locals():
            mysql_connection.close()
        if 'sqlserver_connection' in locals():
            sqlserver_connection.close()








