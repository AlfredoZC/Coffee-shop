import libraries as lbs
import connection

def show_tables(cursor_mysql):
    cursor_mysql.execute("SHOW TABLES")
    saver = cursor_mysql.fetchall()
    for fila in saver:
        print(fila)
    
def select(cursor_mysql, cursor_sqlserver): 
    print("Cual es el nombre de su tabla?")
    show_tables() # Llama a la funcion que muestra todas las tablas.
    activator = True 
    answer = ""
    while activator == True: 
        answer = input("Ingrese el nombre de la tabla: ")
        if answer == "":
            print("No ingreso el nombre de la tabla, intente de nuevo")
            continue
        else: 
            activator = False 
    
    print(""""Que accion """)
    asnwer2 = input("")






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