class KpopShop:
    #diccionario 1
    def dicc_cliente(self):
        cliente={
        "id Cliente:": 1330,
        "Nombre:": "Ailin ruvalcaba",
        "edad:": "25 años",
        "sexo:": "masculino",
        "No.Telefono:":656_263_87_34,   
        "Direccion:":"calle mora #3865",   
        "Forma de pago:":"Tarjeta de credito\n"       
        }
        print(cliente)
        for b,n in cliente.items():
            print(b,n)
    #diccionario 2
    def dicc_producto(self):
        prod= {
        "id producto:": 1234,
        "precio:": "340$",
        "stock:": "1250 piezas",
        "descuento:": "20%",
        "vendedor:":"renata lopez",   
        "fecha:":"12/03/2020",   
        "horario:":"6:46 pm\n"    
        }   
        print(prod)
        for x,c in prod.items():
            print(x,c)
            
    #diccionario 3
    def dicc_empleados(self):
        empleado={
        "id empelado:": 4589,
        "Nombre:": "Valentina Maldonado",
        "edad:": "36 años",
        "sexo:": "femenino",
        "correo:":"valentina_mald18@gmail.com",   
        "No.Telefono:": 656_130_67_02,   
        "Puesto:":"Gerente\n"        
        }
        print(empleado)
        for a,s in empleado.items():
            print(a,s)
    #diccionario 4
    
    def dicc_sucursales(self):
        sucursales={
        "id sucursal:": 1464,
        "Nombre:": "Sucursal las torres",
        "Direcciom:": "calle juan felipe rico #6950",
        "telefono:": 656_580_90_61,
        "horario:":"8am a 12 am",   
        "Empleados:":"130 empleados",   
        "correo:":"kpopShoplastorres@gmail.com\n"        
        }
        print(sucursales)
        for z,v in sucursales.items():
            print(z,v)
    
kpop=KpopShop()
print("\nCliente")
kpop.dicc_cliente()
print("producto")
kpop.dicc_producto()
print("empelado")
kpop.dicc_empleados()
print("sucursales")
kpop.dicc_sucursales()

