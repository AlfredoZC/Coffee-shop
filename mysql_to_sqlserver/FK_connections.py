import connection

def foreing_keys(sqlserver_config):
    try:
        sqlserver_connection = connection.sqlserver_connection(sqlserver_config)
        sqlserver_cursor = sqlserver_connection.cursor()
        
        query = [ """ALTER TABLE pedidos 
                    ADD CONSTRAINT FK_pedidos_clientes 
                    FOREIGN KEY (IDCliente) REFERENCES clientes(IDCliente)
                    ON DELETE CASCADE""",

                """ALTER TABLE pedidos 
                    ADD CONSTRAINT FK_pedidos_empleados 
                    FOREIGN KEY (IDEmpleado) REFERENCES empleados(IDEmpleado)
                    ON DELETE SET NULL""",
                    
                    """ALTER TABLE detallespedido 
                    ADD CONSTRAINT FK_DetallesPedido_pedidos 
                    FOREIGN KEY (IDPedido) REFERENCES pedidos(IDPedido)
                    ON DELETE CASCADE""",
                    
                    """ALTER TABLE detallespedido 
                    ADD CONSTRAINT FK_DetallesPedido_producto 
                    FOREIGN KEY (IDProducto) REFERENCES producto(IDProducto)
                    ON DELETE CASCADE""",
                    
                    """ALTER TABLE pagos 
                    ADD CONSTRAINT FK_pagos_pedidos 
                    FOREIGN KEY (IDPedido) REFERENCES pedidos(IDPedido)
                    ON DELETE CASCADE"""
                    
                    ]
        for consulta in query:
            sqlserver_cursor.execute(consulta)
        sqlserver_connection.commit()
        
    except Exception as e: 
        print("Error al conectar las tablas:" , e)