import libraries as lbs
import connection

def show_tables(cursor_mysql):
    cursor_mysql.execute("SHOW TABLES")
    saver = cursor_mysql.fetchall()
    for fila in saver:
        print(fila)

def get_table(cursor_mysql, table_name):
    cursor_mysql.execute(f"SELECT * FROM {table_name}")
    result = cursor_mysql.fetchall()
    for data in result: 
        print(data)

def select(cursor_mysql, cursor_sqlserver): 

    print("Cual es el nombre de su tabla?")
    show_tables(cursor_mysql) # Llama a la funcion que muestra todas las tablas.
    activator = True 
    table_name = ""
    while activator == True: 
        table_name = input("Ingrese el nombre de la tabla: ")
        if table_name == "":
            print("No ingreso el nombre de la tabla, intente de nuevo")
            continue
        else: 
            activator = False 
    print("El contenido de la tabla es: ")
    get_table(cursor_mysql, table_name)
    print("")

    print(""""Que accion desea realizar?:
              1.- Mostrar una columna  
              2.- Motrar columnas
              3.- Delete
              4.- Modificar
            """)

    answer2 = input("seleccione el numero de su opción: ")

    if answer2 == 1:
        activator = True
        while activator == True:
            column = input("Ingrese la columna: ")
            try:
                mysql_cursor.execute(f"Select {column} From {table_name} ")
                results = mysql_cursor.fetchall()
                for fila in results:
                    print(fila)
                print("Desea ver alguna otra columna? ")    

            #usamos Programing Error en este caso para levanta errores de sintaxis en este caso si la columna no existel.
      
            except lbs.pymysql.err.ProgrammingError as e: 
                print(f"Error de programacion: {e}")
                                                        

        

    elif answer2 == 2:
        pass
    elif answer2 == 3:
        pass
    elif answer2 == 4:
        pass
    
    




print ("Bienvenido a la APP YOUR DATA BASE!. ")
print ("Ingresa los datos de tu BD en MYSQL ")
host = input("host: ")
user = input("user: ")
password = input("password: ")
database = input("database: ")

mysql_config = { #DICCIONARIO CON LOS DATOS DEL USUARIO Y LA BD EN MYSQL
    'host': host,
    'user':user,
    'password':password,
    'database' : database 
}
mysql_connection = connection.mysql_connection(mysql_config)
mysql_cursor = mysql_connection.cursor()

print("") 
print ("Ahora ingresa los datos de tu BD en SQL Server ")
server2 = input("Server: ") #DESKTOP-5J8FKMK
database2 = input("Database: ")

sqlserver_config = { #DICCIONARIO CON LOS DATOS DEL USUARIO Y LA BD EN SQLSERVER
    'Driver': 'ODBC Driver 17 for SQL Server',
    'Server': server2,
    'Database':database2,
    'Trusted_Connection' : 'yes'   
}
sql_server_connection = connection.sqlserver_connection(sqlserver_config) 
sqlserver_cursor =sql_server_connection.cursor()   

select(mysql_cursor, sqlserver_cursor)