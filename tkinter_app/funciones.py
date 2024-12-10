import pymysql

class Funciones:
    def __init__(self):
        host = "localhost"  
        user = "root"       
        password = "241205nico"   
        database = "cafeteria"  
        try:
            self.conexion = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            print("Conexión exitosa a la base de datos.")
        except pymysql.MySQLError as e:
            print(f"Error al conectar{e}")
    def select(self,tabla):
        try:
            cursor=self.conexion.cursor()
            
            consulta = f"SELECT * FROM {tabla} ;"  
            cursor.execute(consulta)

        
            resultados = cursor.fetchall()
            cursor.close()
            return resultados
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None
    
    def describe(self,tabla):
        try:
            cursor = self.conexion.cursor()
            
            consulta = f"DESCRIBE {tabla}"
            cursor.execute(consulta)
            resultados=[fila[0]for fila in cursor.fetchall()]  
            
            return resultados 
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None



            
    def insert_to(self,NombreTabla,val1,val2,val3,valor1,valor2,valor3):
        try:
                
                cursor=self.conexion.cursor()
                consulta=f'''INSERT INTO {NombreTabla}({val1},{val2},{val3})
                            VALUES
                            (%s,%s,%s)
                            '''
                cursor.execute(consulta,(valor1,valor2,valor3))
                self.conexion.commit()
                
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta:{e}")
            return None
    def insert_to2(self,NombreTabla,val1,val2,val3,val4,valor1,valor2,valor3,valor4):
        try:
                
                cursor=self.conexion.cursor()
                consulta=f'''INSERT INTO {NombreTabla}({val1},{val2},{val3},{val4})
                            VALUES
                            (%s,%s,%s,%s)
                            '''
                cursor.execute(consulta,(valor1,valor2,valor3,valor4))
                self.conexion.commit()
                
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta:{e}")
            return None
        
    def delete(self,tabla,campo,valor):
        
        try:
            cursor = self.conexion.cursor()
            
            consulta = "DELETE FROM `{}` WHERE `{}` = %s".format(tabla,campo)
            cursor.execute(consulta, (valor,))  
            self.conexion.commit()
            print(f"Se elimino correctamente de la tabla: {tabla}, el valor: {valor}")
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None
        
        
    def modificar(self,tabla,columna,nuevoValor,campoID,Id):
        
        try:
            cursor = self.conexion.cursor()
            
            consulta = f"UPDATE {tabla} SET {columna}=%s WHERE {campoID}=%s"      
            cursor.execute(consulta,(nuevoValor,Id))  
            self.conexion.commit()
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None
