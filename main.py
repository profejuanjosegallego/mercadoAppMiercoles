#Programa para gestion de productos
#En una lista de mercado
nombreUsuario=None

#Declarando las variables
productos=[]
producto={}

#crear un menu de opciones
print("*** MerqueoAPP ***")
print("1. Agregar Producto a tu lista de mercado")
print("2. Mostrar tu lista de mercado")
print("3. Modificar tu lista de mercado")
print("4. Retirar producto de tu lista de mercado")
print(" Presiona 5 para SALIR")

opcion=100
while opcion != 5:
    opcion=int(input("Digita una opcion del menu: "))

    if opcion == 1:

        #Poblando listas y diccionarios en python 
        #Asignando claves a un diccionario
        producto["id"]=5 #generar de forma aleatoria este numero (unico)
        producto["nombre"]=input("Digita el nombre del producto: ")
        producto["presentacion"]=input(" Digita la presentacion del producto: ")
        producto["cantidad"]=int(input("Digita la cantidad: "))
        producto["precio"]=int(input("Digita el precio del producto: "))

        #Asignando a una lista un diccionario
        productos.append(producto)
        
    elif opcion == 2:
       
        #Recorrer una lista
        for productoIterado in productos:
            print(productoIterado["nombre"])
            print(productoIterado["precio"])

    elif opcion == 3:
        
        # Preguntarle al usuario cual producto quiere cambiar
        idProductoABuscar=int(input("Cual es el id del producto a modificar"))
        # Recorrer la lista para buscar el elemento que quiero modificar
        for productoBuscado in productos:
            if idProductoABuscar==productoBuscado["id"]:
                print("encontrado")
            else:
                print("no encontrado")
        # modificar la o las propiedades pedidas

    elif opcion == 4:
        print("Retirando un producto")
    else:
        print("Opcion invalida")
    
    
