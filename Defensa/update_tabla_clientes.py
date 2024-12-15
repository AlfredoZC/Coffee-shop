from tkinter_app.funciones import *

conexion_base_de_datos=Funciones()

#funcion para obtener los nombres solo de la tabla clientes
def obtener_nombres(tabla):
        
        try:
            cursor = conexion_base_de_datos.conexion.cursor()
            if tabla=="clientes":
                consulta = f"SELECT Nombre FROM {tabla}"      
                cursor.execute(consulta)
                resultados = cursor.fetchall()
                return resultados
        except pyodbc.Error as e:
            return str(e) 


def insertar_valores_palindromo(ids,valores):
        try:
            cursor = conexion_base_de_datos.conexion.cursor()
            consulta = '''UPDATE clientes SET es_palindroma = ? WHERE IDCliente = ?'''
            for i in range(len(ids)):
                id_val = ids[i]
                valor = valores[i]
                cursor.execute(consulta, (valor, id_val))
            conexion_base_de_datos.conexion.commit()  
            return True
        except pyodbc.Error as e:
            return str(e)
        except ValueError as ve:
            return str(ve)
