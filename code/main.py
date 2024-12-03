import libraries as lbs
import connection 

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
server2 = input("Server: ")
database2 = input("Database: ")

sqlserver_config = { #DICCIONARIO CON LOS DATOS DEL USUARIO Y LA BD EN SQLSERVER
    'Driver': 'ODBC Driver 17 for SQL Server',
    'Server': server2,
    'Database':database2,
    'Trusted_Connection' : 'yes'   
}
sql_server_connection = connection.sqlserver_connection(sqlserver_config)





