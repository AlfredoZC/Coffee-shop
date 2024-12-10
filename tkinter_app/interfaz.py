from tkinter import *
from tkinter import ttk
from funciones import *
class Interfaz(Frame):
    funciones=Funciones()
    
    def __init__(self, master = None):
        super().__init__(master, bg = "#6F4E37", height = 400, width = 840)
        self.master=master
        self.master.resizable(False,False)
        self.master.iconbitmap("coffee-cup.ico")
        self.pack()
        self.objetos()
        
    #ocultar interfaces
    def ocultar_mostrar(self,bloque_a_ocultar,bloque_a_mostrar):
        if bloque_a_ocultar:
            bloque_a_ocultar.place_forget()
        if bloque_a_mostrar:
            bloque_a_mostrar.place(x=20,y=20,height=355,width=150)
    def ocultar_mostrarForm(self,bloque_a_ocultar,bloque_a_mostrar):
        if bloque_a_ocultar:
            bloque_a_ocultar.place_forget()
        if bloque_a_mostrar:
            bloque_a_mostrar.place(x=20,y=20,height=355,width=180)
  
    #limpiar datos
    def limpiar_database(self):
        for datos in self.vista_database.get_children():
            self.vista_database.delete(datos)
    def limpiarFormulario(self):
        for widget in self.Formulario.winfo_children():
            widget.destroy()
    
    def limpiar_entrys(self,entrys):
        for i in entrys:
            i.delete(0,END)
        entrys[0].focus()

    #metodos de las interfaces
    def ver_tabla(self,tabla):
        datos=self.funciones.select(tabla)
        columnas=self.funciones.describe(tabla)
        self.vista_database['columns']=columnas
        for x in columnas:
            self.vista_database.column(x,width=120,anchor=CENTER)
            self.vista_database.heading(x,text=x,anchor=CENTER)
        self.vista_database['show']='headings'
        
        if self.ver_tabla:
            self.limpiar_database()
        
        for dato in datos:
            self.vista_database.insert("",END,values=(dato))
    
    def guardar_agregar(self):
        lista=[]
        results=self.resultados
        
        for i in range(len(self.entrys)):
            lista.append(self.entrys[i].get())
        
        lista2=[]
        for j in lista:
            if j.isdigit():
                lista2.append(int(j))
            else:
                lista2.append(j)
                
        if len(results)<=4:
            self.funciones.insert_to(self.tabla2,results[1],results[2],results[3],lista2[1],lista2[2],lista2[3])
        else:
            self.funciones.insert_to2(self.tabla2,results[1],results[2],results[3],results[4],lista2[1],lista2[2],lista2[3],lista2[4])
        
        self.limpiar_entrys(self.entrys)
    
    def metodo_agregar(self, tabla):
        self.ver_tabla(tabla)
        self.ocultar_mostrarForm(self.interfaz_agregar,self.Formulario)
        self.tabla2=tabla
        
        self.limpiarFormulario()
        self.resultados = self.funciones.describe(tabla)
        totalResults=len(self.resultados)
        
        
       

        self.labels=[]
        self.entrys=[]
        for i in range(totalResults):  
                label = Label(self.Formulario, text="")
                label.place(x=50, y=10+i*50)  
                self.labels.append(label)
                 #Crear el Entry
                entry1 = Entry(self.Formulario,bg="white")
                entry1.place(x=5, y=37 +i*50, height=20, width=170)
                self.entrys.append(entry1)
 
        
        # Actualizar el texto de los Labels
        for i, label in enumerate(self.labels):
            label.config(text=self.resultados[i] if i < len(self.resultados) else "")
            
        self.guardar = Button(self.Formulario, text="GUARDAR", bg="green",command=self.guardar_agregar)
        self.guardar.place(x=5, y=277, height=35, width=80)
        
        self.cancelar_agregar = Button(self.Formulario, text="CANCELAR", bg="#Ff0000", command=lambda:self.limpiar_entrys(self.entrys))
        self.cancelar_agregar.place(x=95, y=277, height=35, width=80)
        
        self.regresar3 = Button(self.Formulario, text="REGRESAR", bg="#Ff0000", command=lambda:self.ocultar_mostrar(self.Formulario,self.interfaz_agregar))
        self.regresar3.place(x=3, y=315, height=35, width=173)
        
   
    def guardar_modificar(self):
        valor1=self.entrys[0].get()
        valor2=self.entrys[1].get()
        valor3=int(self.entrys[2].get())
        campoID=self.idd
        self.funciones.modificar(self.tabla1,valor1,valor2,campoID,valor3)
        self.limpiar_entrys(self.entrys)
    def metodo_modificar(self,table):
        self.ver_tabla(table)   
        self.ocultar_mostrarForm(self.interfaz_modificar,self.Formulario)
        self.limpiarFormulario()
        self.tabla1=table
        
        self.resultados3 = self.funciones.describe(table)
        self.idd=self.resultados3[0]
        
        self.labels=[]
        self.entrys=[]
        
       

        
         
        label = Label(self.Formulario, text="Columna")
        label.place(x=83, y=65)  
        self.labels.append(label)
        entry1 = Entry(self.Formulario,bg="white")
        entry1.place(x=5, y=100, height=20, width=170)
        self.entrys.append(entry1)
        
        
        label2 = Label(self.Formulario, text="Nuevo Valor")
        label2.place(x=68, y=150)  
        self.labels.append(label2)
        entry2 = Entry(self.Formulario,bg="white")
        entry2.place(x=5, y=170, height=20, width=170)
        self.entrys.append(entry2)
        
        label3 = Label(self.Formulario, text="ID")
        label3.place(x=68, y=220)  
        self.labels.append(label3)
        entry3 = Entry(self.Formulario,bg="white")
        entry3.place(x=5, y=250, height=20, width=170)
        self.entrys.append(entry3)
        #Crear el Entry
        
        
        
        
        
        self.guardar = Button(self.Formulario, text="GUARDAR", bg="green",command=self.guardar_modificar)
        self.guardar.place(x=5, y=277, height=35, width=80)
        
        self.cancelar_modificar = Button(self.Formulario, text="CANCELAR", bg="#Ff0000", command=lambda:self.limpiar_entrys(self.entrys))
        self.cancelar_modificar.place(x=95, y=277, height=35, width=80)
        
        self.regresar3 = Button(self.Formulario, text="REGRESAR", bg="#Ff0000", command=lambda:self.ocultar_mostrar(self.Formulario,self.interfaz_modificar))
        self.regresar3.place(x=3, y=315, height=35, width=173)
        
        
              
    
    def guardar_eliminar(self):
        valor=int(self.entrys[0].get())
        self.funciones.delete(self.table,self.id,valor)
        self.limpiar_entrys(self.entrys)
    def metodo_eliminar(self,tabla):
        self.ver_tabla(tabla)
        self.ocultar_mostrarForm(self.interfaz_eliminar,self.Formulario)
        
        self.limpiarFormulario()
        self.table=tabla
        
        self.resultados2 = self.funciones.describe(tabla)
        self.id=self.resultados2[0]
        
        self.labels=[]
        self.entrys=[]
        
        label = Label(self.Formulario, text="ID")
        label.place(x=83, y=65)  
        self.labels.append(label)
        #Crear el Entry
        entry1 = Entry(self.Formulario,bg="white")
        entry1.place(x=5, y=100, height=20, width=170)
        self.entrys.append(entry1)
        self.guardar = Button(self.Formulario, text="GUARDAR", bg="green",command=self.guardar_eliminar)
        self.guardar.place(x=5, y=277, height=35, width=80)
        
        self.cancelar_eliminar = Button(self.Formulario, text="CANCELAR", bg="#Ff0000", command=lambda:self.limpiar_entrys(self.entrys))
        self.cancelar_eliminar.place(x=95, y=277, height=35, width=80)
        
        self.regresar3 = Button(self.Formulario, text="REGRESAR", bg="#Ff0000", command=lambda:self.ocultar_mostrar(self.Formulario,self.interfaz_eliminar))
        self.regresar3.place(x=3, y=315, height=35, width=173)
        
    
       
    #metodo creacion de interfaz
    def crear_interfaz(self,comandos):
        bloque=Frame(self,bg="#E3E1DC")
        for i,(nombre_boton,comando) in enumerate(comandos):
            boton=Button(bloque,text=nombre_boton,bg="#C19A6B",command=comando)
            boton.place(x=7,y=5+i*50,height=45,width=135)
        boton_regresar = Button(bloque, text="REGRESAR", bg="#Ff0000", command=lambda: self.ocultar_mostrar(bloque,self.bloque_principal))
        boton_regresar.place(x=7, y=5 + len(comandos) * 50, height=45, width=135)
        return bloque
    
        
    def objetos(self):
        #listas de comandos
        self.comandos_ver = [
            ("CLIENTES", lambda: self.ver_tabla('clientes')),
            ("EMPLEADOS", lambda: self.ver_tabla('empleados')),
            ("PRODUCTOS", lambda: self.ver_tabla('producto')),
            ("DETALLES PEDIDOS", lambda: self.ver_tabla('detallespedido')),
            ("PEDIDOS", lambda: self.ver_tabla('pedidos')),
            ("PAGOS", lambda: self.ver_tabla('pagos')),
        ]

        self.comandos_agregar = [
            ("CLIENTES", lambda: self.metodo_agregar('clientes')),
            ("EMPLEADOS", lambda: self.metodo_agregar('empleados')),
            ("PRODUCTOS", lambda: self.metodo_agregar('producto')),
            ("DETALLES PEDIDOS", lambda: self.metodo_agregar('detallespedido')),
            ("PEDIDOS", lambda: self.metodo_agregar('pedidos')),
            ("PAGOS", lambda: self.metodo_agregar('pagos')),
        ]

        self.comandos_modificar = [
            ("CLIENTES", lambda: self.metodo_modificar('clientes')),
            ("EMPLEADOS", lambda: self.metodo_modificar('empleados')),
            ("PRODUCTOS", lambda: self.metodo_modificar('producto')),
            ("DETALLES PEDIDOS", lambda: self.metodo_modificar('detallespedido')),
            ("PEDIDOS", lambda: self.metodo_modificar('pedidos')),
            ("PAGOS", lambda: self.metodo_modificar('pagos')),
        ]

        self.comandos_eliminar = [
            ("CLIENTES", lambda: self.metodo_eliminar('clientes')),
            ("EMPLEADOS", lambda: self.metodo_eliminar('empleados')),
            ("PRODUCTOS", lambda: self.metodo_eliminar('producto')),
            ("DETALLES PEDIDOS", lambda: self.metodo_eliminar('detallespedido')),
            ("PEDIDOS", lambda: self.metodo_eliminar('pedidos')),
            ("PAGOS", lambda: self.metodo_eliminar('pagos')),
        ]
        
        #creacion de la interfaz principal
        self.bloque_principal=Frame(self,bg="#F5EDE1")
        self.bloque_principal.place(x=20,y=20,height=355,width=150)
        self.ver=Button(self.bloque_principal,text="VER",bg="#C19A6B",command=lambda:self.ocultar_mostrar(self.bloque_principal,self.interfaz_vista))
        self.ver.place(x=7,y=10,height=80,width=135) 
        self.agregar=Button(self.bloque_principal,text="AGREGAR",bg="#C19A6B",command=lambda:self.ocultar_mostrar(self.bloque_principal,self.interfaz_agregar))
        self.agregar.place(x=7,y=95,height=80,width=135)
        self.modificar=Button(self.bloque_principal,text="MODIFICAR",bg="#C19A6B",command=lambda:self.ocultar_mostrar(self.bloque_principal,self.interfaz_modificar))
        self.modificar.place(x=7,y=180,height=80,width=135)
        self.eliminar=Button(self.bloque_principal,text="ELIMINAR",bg="#C19A6B",command=lambda:self.ocultar_mostrar(self.bloque_principal,self.interfaz_eliminar))
        self.eliminar.place(x=7,y=265,height=80,width=135)
        
        #creacion de las diferentes vistas de las interfaces
        self.interfaz_vista=self.crear_interfaz(self.comandos_ver)        
        self.interfaz_agregar=self.crear_interfaz(self.comandos_agregar)
        self.interfaz_modificar=self.crear_interfaz(self.comandos_modificar)
        self.interfaz_eliminar=self.crear_interfaz(self.comandos_eliminar)
        
        #creacion del formulario
        self.Formulario=Frame(self,bg="#E3E1DC")
        
        #creacion del treeview (hace que se vea la base de datos)
        self.vista_database=ttk.Treeview(self)
        self.vista_database.place(x=220,y=18,width=600,height=355)
   
        
raiz=Tk()
raiz.wm_title("Cafetería")

app=Interfaz(raiz)

app.mainloop()