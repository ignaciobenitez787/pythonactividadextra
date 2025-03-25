inventario = {}
leave = False
options = ["1. Agregar o modificar un producto", "2. Mostrar el inventario", "3. Eliminar un producto", "4. Salir del programa"]
while leave == False:
        print("¿Que desea hacer?")
        for option in options:
                print(option)
        user_input = input("Seleccione una opción \n")
        if user_input.isdigit():
                user_input=int(user_input)
        else:
            print("Respuesta no valida")
            continue
        match user_input:
                case 1: 
                    producto = input("Ingrese el producto a añadir o modificar: ")
                    while True:
                        cantidad = input("Ingrese la cantidad del producto: ")
                        if cantidad.isdigit and int(cantidad)>0:
                              cantidad = int(cantidad)
                              inventario[producto] = cantidad
                              print("Operación realizada correctamente")
                              break
                        else:
                            print("Cantidad invalida")
                case 2:
                    for producto, cantidad in inventario.items():
                          print("Producto: ", producto, " Cantidad: ", cantidad)
                    if (not inventario):
                          print("El inventario está vacio")
                case 3: 
                    producto = input("Ingrese el producto a eliminar: ")
                    if producto in inventario:
                          del inventario[producto]
                          print("Operación realizada correctamente")
                    else:
                          print("El producto no se encuentra en el inventario")
                case 4:
                    leave = True
                case _:
                    print("Opción no valida")
                    
            

                    
                    

