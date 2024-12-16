import libraries as lbs

def sqlserver_connection(sqlserver_config):
    try:

        connection = lbs.pyodbc.connect(
            
                    f"Driver={sqlserver_config['Driver']};"
                    f"Server={sqlserver_config['Server']};"
                    f"Database={sqlserver_config['Database']};"
                    f"Trusted_Connection={sqlserver_config['Trusted_Connection']};"

        )
        print("Conexion Exitosa!")
        return connection
    
    except lbs.pyodbc.Error as e:
        print("Error al conectar a SQL server:", e )
        raise

def mysql_connection(mysql_config) : # FUNCION QUE NOS PERMITIRA CONECTARNOS A LA BASE DE DATOS SIN TENER QUE ESCRIBIR DE MAS
    try: 
        connection = lbs.pymysql.connect(
            host = mysql_config['host'],
            user = mysql_config['user'],
            password = mysql_config['password'],
            database=  mysql_config['database']
        )
        print("Conexion Exitosa!")
        return connection
    
    except lbs.pymysql.MySQLError as e:
        print (f"error al conectar : {e}")
        raise


