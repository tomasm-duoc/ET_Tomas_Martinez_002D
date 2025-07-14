productos = {'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],}
             
stock = {
         'GF75HD': [749990,2],
         'JjfFHD': [424990,1],
         'UWU131HD': [349990,1],
         'fgdxFHD': [664990,21],
         '123FHD': [290890,32],
         '2175HD': [327990,4],
         '342FHD': [444990,7],
         '8475HD': [387990,10],
         'FS1230HD': [249990,0]}

def verificacion_entero(mensaje:str):
    try:
        numero = int(input(mensaje))
    except ValueError:
        print("ERROR - Ingrese un valor númerico.")
        return False
    else:
        return numero
    
def verificacion_texto(mensaje:str):
    while True:
        texto = input(mensaje)
        if len(texto.strip()) < 1:
            print("ERROR - No puede ingresar un texto vacio.")
        else:
            return texto
    
def stock_marca(marca:str):
    stock_funcion = 0
    for i in productos:
        if productos[i][0].lower() == marca.lower():
            stock_funcion += stock[i][1]
    print(f"\nEl stock de {marca} es: {stock_funcion}")

def busqueda_precio(p_min:int,p_max:int):
    productos_dentro_rango = []
    for i in stock:
        if stock[i][0] >= p_min and stock[i][0] <= p_max:
            if stock[i][1] < 1:
                continue    
            else:    
                productos_dentro_rango.append(f"{productos[i][0]}--{i}")
    if len(productos_dentro_rango) < 1:
        print("\nNo hay notebooks en ese rango de precios.")
    else:
        print(f"Los notebooks entre los precios consultas son: {productos_dentro_rango}")

def actualizar_precio(modelo:str,p:int):
    for i in stock:
        if modelo == i:
            stock[i][0] = p
            return True
    return False


while True:
    print("\n*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")

    opcion = verificacion_entero("\nIngrese una opción: ")

    if opcion == 1:
        marca = verificacion_texto("\nIngrese la marca que desea buscar: ")
        stock_marca(marca)

    elif opcion == 2:
        while True:
            precio_minimo = verificacion_entero("\nIngrese el precio minimo de búsqueda: ")
            if precio_minimo == False:
                continue
            precio_maximo = verificacion_entero("\nIngrese el precio maximo de búsqueda: ")
            if precio_maximo == False:
                continue
            if precio_minimo > precio_maximo:
                print("\nERROR - Ingrese los valores de precio en el orden correcto.")
                continue

            busqueda_precio(precio_minimo,precio_maximo)
            break

    elif opcion == 3: #actualizar
        while True:
            modelo = verificacion_texto("\nIngrese el modelo que desea actualizar: ")
            precio = verificacion_entero("Ingrese el nuevo precio del modelo: ")

            verificacion = actualizar_precio(modelo,precio)
            if verificacion == True:
                print("\nPrecio actualizado correctamente!")
                actualizar_de_nuevo = verificacion_texto("\nDesea actualizar el precio de otro notebook (s/n): ")
                if actualizar_de_nuevo.lower() == "si" or actualizar_de_nuevo.lower() == "s":
                    continue
                else:
                    break
                    
            elif verificacion == False:
                print("\nEse modelo no existe!!!")
                actualizar_de_nuevo = verificacion_texto("\nDesea actualizar el precio de otro notebook (s/n): ")
                if actualizar_de_nuevo.lower() == "si" or actualizar_de_nuevo.lower() == "s":
                    continue
                else:
                    break

    elif opcion == 4:
        break
    
    else:
        print("Ingrese una opción valida!!!")

print("Programa finalizado.")