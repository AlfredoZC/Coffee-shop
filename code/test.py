import pymysql
import pyodbc

class Table:
    def __init__(self, name, columns, rows):
        self.name = name      # Nombre de la tabla
        self.columns = columns  # Lista de columnas
        self.rows = rows      # Lista de filas

    def __repr__(self):
        return f"Table(name={self.name}, columns={self.columns}, rows={len(self.rows)} filas)"

def obtener_tablas_mysql(cursor):
    """Obtiene todas las tablas de la base de datos MySQL."""
    cursor.execute("SHOW TABLES")
    return [row[0] for row in cursor.fetchall()]

def obtener_columnas_mysql(cursor, tabla):
    """Obtiene todas las columnas de una tabla MySQL."""
    cursor.execute(f"DESCRIBE {tabla}")
    return [row[0] for row in cursor.fetchall()]

def obtener_datos_mysql(cursor, tabla, columnas):
    """Obtiene todos los datos de una tabla MySQL."""
    column_list = ', '.join(columnas)
    cursor.execute(f"SELECT {column_list} FROM {tabla}")
    return cursor.fetchall()

def migrar_mysql_a_sqlserver(mysql_config, sqlserver_config):
    """
    Migra todas las tablas de una base de datos MySQL a SQL Server.

    Args:
        mysql_config (dict): Configuración de la conexión MySQL.
        sqlserver_config (dict): Configuración de la conexión SQL Server.
    """
    try:
        # Conexión a MySQL
        mysql_conn = pymysql.connect(**mysql_config)
        mysql_cursor = mysql_conn.cursor()

        # Conexión a SQL Server
        sqlserver_conn = pyodbc.connect(
            f"DRIVER={sqlserver_config['driver']};"
            f"SERVER={sqlserver_config['server']};"
            f"DATABASE={sqlserver_config['database']};"
            f"UID={sqlserver_config['user']};"
            f"PWD={sqlserver_config['password']}"
        )
        sqlserver_cursor = sqlserver_conn.cursor()

        # Lista de objetos Table
        tablas = []

        # Obtener todas las tablas
        nombres_tablas = obtener_tablas_mysql(mysql_cursor)
        for nombre_tabla in nombres_tablas:
            print(f"Cargando datos de la tabla: {nombre_tabla}")

            # Obtener columnas y datos
            columnas = obtener_columnas_mysql(mysql_cursor, nombre_tabla)
            filas = obtener_datos_mysql(mysql_cursor, nombre_tabla, columnas)

            # Crear un objeto Table y añadirlo a la lista
            tabla = Table(name=nombre_tabla, columns=columnas, rows=filas)
            tablas.append(tabla)

        # Migrar los datos
        for tabla in tablas:
            print(f"Migrando tabla: {tabla.name}")
            columnas = tabla.columns
            filas = tabla.rows

            # Crear consulta dinámica
            column_list = ', '.join(columnas)
            placeholders = ', '.join(['?'] * len(columnas))
            insert_query = f"INSERT INTO {tabla.name} ({column_list}) VALUES ({placeholders})"

            # Insertar datos
            for fila in filas:
                sqlserver_cursor.execute(insert_query, fila)

            # Confirmar cambios
            sqlserver_conn.commit()

        print("Migración completada para todas las tablas.")
    except Exception as e:
        print(f"Error durante la migración: {e}")
    finally:
        # Cerrar conexiones
        if 'mysql_conn' in locals():
            mysql_conn.close()
        if 'sqlserver_conn' in locals():
            sqlserver_conn.close()

# Configuración de la conexión MySQL
mysql_config = {
    "host": "tu_host_mysql",
    "user": "tu_usuario_mysql",
    "password": "tu_contraseña_mysql",
    "database": "tu_base_datos_mysql"
}

# Configuración de la conexión SQL Server
sqlserver_config = {
    "driver": "ODBC Driver 17 for SQL Server",
    "server": "tu_servidor_sqlserver",
    "database": "tu_base_datos_sqlserver",
    "user": "tu_usuario_sqlserver",
    "password": "tu_contraseña_sqlserver"
}

# Llamada a la función principal
migrar_mysql_a_sqlserver(mysql_config, sqlserver_config)
