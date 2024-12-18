import mysql_to_sqlserver.funciones_migracion as migrate
import mysql_to_sqlserver.llaves_foraneas as FK 

try:

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


    print("") 
    print ("Ahora ingresa los datos de tu BD en SQL Server ")
    server2 = input("Server: ") 
    database2 = input("Database: ")

    sqlserver_config = { #DICCIONARIO CON LOS DATOS DEL USUARIO Y LA BD EN SQLSERVER
        'Driver': 'ODBC Driver 17 for SQL Server',
        'Server': server2, #HP
        'Database':database2, #cafeteria_new
        'Trusted_Connection' : 'yes'   
    }

    migrate.migrate_mysql_to_sqlserver(mysql_config, sqlserver_config)
    print("")
    print("Conectando tablas y sus llaves: ")
    FK.foreing_keys(sqlserver_config)
    print("Migracion exitosa! ")

except Exception as e:

    print("Ocurrio un error:", e)
            