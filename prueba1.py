#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], 

productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
 '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
 'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
 'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
 'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
 '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
 '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
 'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'], 
 }

#stock = modelo: [precio, stock], ...]
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
 'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
 'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
 }




def stock_marca(marca):
    found = False
    for modelo, detalles in productos.items():
        if detalles[0] == marca:
            found = True
            if modelo in stock:
                print(f"Modelo: {modelo}, Stock: {stock[modelo][1]}")
            else:
                print(f"Modelo: {modelo}, Stock: No disponible")
    if not found:
        print("Marca no encontrada, ingrese marca nuevamente")
        
def busqueda_precio(p_min, p_max):
    try:
        p_min = int(p_min)
        p_max = int(p_max)
    except ValueError:
        print("Debe ingresar valores enteros!!")
        return
    resultados = []
    for modelo, detalles in productos.items():
        marca, precio, stock = detalles
        if p_min <= precio <= p_max and stock > 0:
            resultados.append(f"{marca}--{modelo}")
    if resultados:
        resultados.sort()  
        print("Modelos disponibles en el rango de precios:")
        for resultado in resultados:
            print(resultado)
    else:
        print("No hay notebooks en ese rango de precios.")

                       

def menu (): 
    while True:
        print ("*** MENU PRINCIPAL Pybooks ***")
        print ("1. Stock marca.")
        print ("2. Búsqueda por precio.")
        print ("3. Actualizar precio.")
        print ("4. Salir")
        menu=int(input("ingrese opcion: "))
        if menu == 1:
            stock_marca(input("ingrese marca: "))
        elif menu == 2:
            p_min = input("Ingrese precio mínimo: ")
            p_max = input("Ingrese precio máximo: ")
            busqueda_precio(p_min, p_max)
        #elif menu == 3:
            #actualizar_precio(input("ingrese valor: "))
        elif menu == 4:
            print ("Adios!!!!")
            break

          
                         
menu ()



