#just for testing..

import libraries as lbs

try:
    connection_sql_server = lbs.pyodbc.connect(
            
                "Driver=ODBC Driver 17 for SQL Server;"
                "Server=HP;"
                "Database=cafeteria_new;"
                "Trusted_Connection=yes;"

        )
    print("Conexion Exitosa!")
    
except lbs.pyodbc.Error as e:
        print("Error al conectar a SQL server:", e )
        raise

try: 
    connection_mysql_server = lbs.pymysql.connect(
            host ='localhost',
            user = 'root',
            password = '333666999A.z',
            database= 'cafeteria' 
        )
    print("Conexion Exitosa!")
        
    
except lbs.pymysql.MySQLError as e:
        print (f"error al conectar : {e}")
        raise

try:
    cursor_mysql = connection_mysql_server.cursor() 
    cursor_mysql.execute("SHOW TABLES ")
    result1 = [row[0] for row in cursor_mysql.fetchall()]  # recojemos todas las tablas de la columna 0
    counter1= 0 
    for i in result1:
        counter1 += 1

    cursor_slq_server = connection_sql_server.cursor()
    cursor_slq_server.execute("""SELECT TABLE_NAME
                                FROM INFORMATION_SCHEMA.TABLES
                                WHERE TABLE_TYPE = 'BASE TABLE';""")
    
    result2 = [row[0] for row in cursor_slq_server.fetchall()] # recojemos todas las tablas de la columna 0
    counter2 = 0
    for i in result2:
         if i == 'sysdiagrams':
              pass
         else:
            counter2 +=1

    if counter1 == counter2 :
         print("Tienen las mismas tablas!!")
    else:
         print("No tienen las mismas tablas :( ")

except Exception as e: 
      print("Error al hacer la consulta:" ,e)

finally:
    
    if connection_mysql_server is not None:
        connection_mysql_server.close()
        print("Conexión a MySQL cerrada.")
    if connection_sql_server is not None:
        connection_sql_server.close()
        print("Conexión a SQL Server cerrada.")

