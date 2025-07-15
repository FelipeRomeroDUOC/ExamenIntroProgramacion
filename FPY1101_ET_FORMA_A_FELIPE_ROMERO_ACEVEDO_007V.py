import time

productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {
    '8475HD': [387990,10], 
    '2175HD': [327990,4], 
    'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], 
    '123FHD': [290890,32], 
    '342FHD': [444990,7],
    'GF75HD': [749990,2], 
    'UWU131HD': [349990,1], 
    'FS1230HD': [249990,0]}

def stock_marca(marca = 'LENOVO'): 
    stockmarca = 0
    for producto in productos:
        marcadelproducto = productos[producto][0]
        marcadelproducto = marcadelproducto.upper()

        if marca == marcadelproducto:
            stockproducto = stock[producto][1]
            stockmarca += stockproducto
    print(f"El stock es: {stockmarca}")

#stock_marca() -- TEST

def busqueda_precio(p_min = 0, p_max = 100000):
    lista_productos = []
    for producto in stock:
        precio = stock[producto][0]
        if precio in range(p_min, p_max +1):
            try:
                marca = productos[producto][0]
                modelo = producto
                lista_productos.append(f"{marca}--{modelo}")
                #print(lista_productos) -- DEBUG
            except KeyError:
                continue
    if lista_productos == []:
        print("No hay notebooks en este rango de precios.")
    else:
        lista_productos.sort()
        print(lista_productos)

#busqueda_precio() -- TEST

def actualizar_precio(modelo = '8475HD', precio = 999999):
    for producto in stock:
        if producto == modelo:
            stock[producto][0] = precio
            return True
    return False

'''
print(stock['8475HD'])
actualizar_precio()
print(stock['8475HD'])
'''
# -- TEST

def main():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")
        
        lista_marcas = []
        for producto in productos:
            marcaprod = productos[producto][0]
            marcaprod = marcaprod.upper()
            if marcaprod not in lista_marcas:
                lista_marcas.append(marcaprod)

        while True:
            opcion = input("\nIngrese una opción (1-4): ")

            if opcion not in '1234':
                print("¡Debe seleccionar una opción válida!\n")
                time.sleep(1)
            else: break

        if opcion == '1':
            marca = input("\nIngrese marca a consultar: ")
            marca = marca.upper()
            if marca not in lista_marcas:
                print("La marca ingresada no existe en la base de datos, por favor intente con otra marca.")
                time.sleep(1)
            else:
                stock_marca(marca)
                time.sleep(1)
        
        elif opcion == '2':
            while True:
                try:
                    p_min = int(input("\nIngrese precio mínimo: "))
                    if p_min < 0:
                        print("¡Debe ingresar valores positivos!")
                    else: break
                except ValueError:
                    print("¡Debe ingresar valores enteros!")
                    time.sleep(1)
            while True:
                try:
                    p_max = int(input("Ingrese precio máximo: "))
                    if p_max < 0:
                        print("¡Debe ingresar valores positivos!")
                    else:
                        busqueda_precio(p_min, p_max)
                        time.sleep(1)
                        break
                except ValueError:
                    print("¡Debe ingresar valores enteros!")
                time.sleep(1)
        
        elif opcion == '3':
            while True:
                modelo = input("\nIngrese modelo a actualizar: ")
                if modelo not in stock:
                    print("¡El modelo no existe!")
                else:
                    while True:
                        try:
                            precioactualizado = int(input("\nIngrese precio nuevo: "))
                            if precioactualizado < 0:
                                print("¡Debe ingresar valores positivos!")
                            else:
                                actualizar_precio(modelo, precioactualizado)
                                print("¡Precio actualizado!")
                                break
                        except ValueError:
                            print("¡Debe ingresar valores enteros!")
                        time.sleep(1)
                
                loopcheck = True
                while loopcheck:
                    check = input("\n¿Desea actualizar otro precio? (s/n): ")
                    if check in ['S', 's', 'si', 'Si', 'SI']:
                        break
                    elif check in ['N', 'n', 'no', 'No', 'NO']:
                        loopcheck = False
                    else: 
                        print("¡Ingrese sí o no!")
                        time.sleep(1)

                if not loopcheck: break

        else: 
            print("Programa finalizado.")
            time.sleep(1)
            return
        
main()