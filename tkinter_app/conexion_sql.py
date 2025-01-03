import pyodbc

class Funciones:
    def __init__(self):
        host = "localhost"    
        database = "cafeteria"  
        try:
            self.conexion = pyodbc.connect(
                f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                f'SERVER={host};'
                f'DATABASE={database};'
                f'Trusted_Connection=yes;'
            )
            print("Conexión exitosa a la base de datos.")
        except pyodbc.Error as e:
            print(f"Error al conectar{e}")
    def cerrar_conexion(self):
        try:
            if self.conexion:
                self.conexion.close() 
                print("Conexión cerrada correctamente.")
        except pyodbc.Error as e:
            print(f"Error al cerrar la conexión: {e}")
    def select(self,tabla):
        try:
            cursor=self.conexion.cursor()
            
            consulta = f"SELECT * FROM {tabla} ;"  
            cursor.execute(consulta)

        
            resultados = cursor.fetchall()
            cursor.close()
            
            return resultados
        except pyodbc.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None
    
    def describe(self,tabla):
        try:
            cursor = self.conexion.cursor()
            
            consulta =  f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{tabla}'"
            cursor.execute(consulta)
            resultados=[fila[0]for fila in cursor.fetchall()]  
            
            return resultados 
        except pyodbc.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None



            
    def insert_to(self,NombreTabla,val1,val2,val3,valor1,valor2,valor3):
        try:
                
                cursor=self.conexion.cursor()
                consulta=f'''INSERT INTO {NombreTabla}({val1},{val2},{val3})
                            VALUES
                            (?,?,?)
                            '''
                cursor.execute(consulta,(valor1,valor2,valor3))
                self.conexion.commit()
                return True
        except pyodbc.Error as e:
            return str(e)
    def insert_to2(self,NombreTabla,val1,val2,val3,val4,valor1,valor2,valor3,valor4):
        try:
                
                cursor=self.conexion.cursor()
                consulta=f'''INSERT INTO {NombreTabla}({val1},{val2},{val3},{val4})
                            VALUES
                            (?,?,?,?)
                            '''
                cursor.execute(consulta,(valor1,valor2,valor3,valor4))
                self.conexion.commit()
                return True
        except pyodbc.Error as e:
            return str(e)

        
    def delete(self,tabla,campo,valor):
        
        try:
            cursor = self.conexion.cursor()
            
            consulta = f"DELETE FROM {tabla} WHERE {campo} = ?"
            
            cursor.execute(consulta, valor)  
            self.conexion.commit()
            print(f"Se elimino correctamente de la tabla: {tabla}, el valor: {valor}")
        except pyodbc.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None
        
        
    def modificar(self,tabla,columna,nuevoValor,campoID,Id):
        
        try:
            cursor = self.conexion.cursor()
            
            consulta = f"UPDATE {tabla} SET {columna}=? WHERE {campoID}=?"      
            cursor.execute(consulta,nuevoValor,Id)  
            self.conexion.commit()
            return True
        except pyodbc.Error as e:
            return str(e) 
