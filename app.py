import os
os.system("cls")


def menu_principal():
    print("""===== MENÚ PRINCIPAL =====
          1. Stock por categoría.
          2. Buscar productos por rango de precio.
          3. Actualizar precio.
          4. Agregar producto.
          5. Eliminar producto.
          6. Mostrar productos.
          7. Salir.
          =============================
          """)
    
def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción del menú: "))
            if opcion >= 1 and opcion <= 7:
                return opcion
            else:
                print("Debe seleccionar una opción válida.")
        except ValueError:
            print("Debe ingresar un número de tipo entero.")

def validar_codigo(codigo):
    return codigo.strip() != ""

def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_categoria(categoria):
    return categoria.strip() != ""

def validar_precio(precio):
    return precio > 0

def validar_disponible(disponible):
    disponible = disponible.lower()
    return disponible == "s" or disponible == "n"

def validar_stock(stock):
    return stock >= 0

def validar_vendidos(vendidos):
    return vendidos >= 0

def stock_categoria(categoria, productos, inventario):
    total_stock = 0

    for codigo in productos:
        datos_producto = productos[codigo]
        categoria_producto = datos_producto[1]

        if categoria_producto.lower() == categoria.lower():
            if codigo in inventario:
                stock = inventario[codigo][0]
                total_stock = total_stock + stock

    print(f"Stock total: {total_stock}")

def buscar_precio(productos, inventario, precio_min, precio_max):
    resultados = []

    for codigo in productos:
        precio = productos[codigo][2]
        stock = inventario[codigo][0]

        if precio >= precio_min and precio <= precio_max and stock > 0:
            resultados.append(productos[codigo][0] + "--" + codigo)

    resultados.sort()

    if len(resultados) == 0:
        print("No hay productos en ese rango.")
    else:
        for producto in resultados:
            print(producto)
        

def buscar_codigo(productos, inventario, codigo):
    codigo = codigo.upper()

    if codigo in productos and codigo in inventario:
        return True
    
    return False

def actualizar_precio(productos, inventario, codigo, nuevo_precio):
    codigo = codigo.upper()
    if buscar_codigo(productos, inventario, codigo):
        productos[codigo][2] = nuevo_precio
        return True
    return False
    

def agregar_producto(codigo, nombre, categoria, precio, disponible, stock, vendidos, productos, inventario):
    codigo = codigo.upper()

    if disponible.lower() == "s":
        disponible = True
    else:
        disponible = False

    productos[codigo] = [
        nombre,
        categoria,
        precio,
        disponible
    ]

    inventario[codigo] = [
        stock,
        vendidos
    ]
    return True
def eliminar_producto(codigo, productos, inventario):
    codigo = codigo.upper()

    if buscar_codigo(productos, inventario, codigo):
        del productos[codigo]
        del inventario[codigo]
        return True
    
    return False

def mostrar_producto(productos, inventario):
    for codigo in productos:
        print(codigo, productos[codigo], inventario[codigo])

def ejecutar_stock_categoria(productos, inventario):
    categoria = input("Ingrese categoría de producto: ")
    stock_categoria(categoria, productos, inventario)

def ejecutar_busqueda_precio(productos, inventario):
    while True:
        precio_min = int(input("Ingrese el precio mínimo: "))

        if precio_min >= 0:
            break
        else:
            print("El precio mínimo debe ser mayor a igual a 0.")
    while True:
        precio_max = int(input("Ingrese el precio máximo: "))

        if precio_max >= 0:
            break
        else:
            print("El precio máximo debe ser mayor o igual a 0.")
    if precio_min > precio_max:
        print("El precio mínimo no puede ser mayor que el precio máximo.")
        return
        
    
def ejecutar_actualizar_precio(productos, inventario):
    codigo = input("Ingresar el código del producto:: ")

    while True:
        nuevo_precio = int(input("Ingrese nuevo precio del producto: "))

        if validar_precio(nuevo_precio):
            break
        else:
            print("El precio debe ser mayor que 0.")
    
    actualizado = actualizar_precio(productos, inventario, codigo, nuevo_precio)

    if actualizado:
        print("Precio actualizado.")
    else:
        print("El código no existe.")

def ejecutar_agregar_productos(productos, inventario):
    codigo = input("Ingrese código del producto: ").upper()

    if not validar_codigo(codigo):
        print("El código no puede estar vacío.")
        return

    if buscar_codigo(productos, inventario, codigo):
        print("El código ya existe.")
        return
    
    while True:
        nombre = input("Ingrese nombre: ")

        if validar_nombre(nombre):
            break
        else:
            print("El nombre no puede estar vacío.")

    while True:
        categoria = input("Ingrese categoría: ")

        if validar_categoria(categoria):
            break
        else:
            print("La categoría no puede estar vacía.")
    
    while True:
        try:
            precio = int(input("Ingrese precio: "))

            if validar_precio(precio):
                break
            else:
                print("El precio debe ser mayor que 0.")

        except:
            print("Debe ingresar un número entero.")

    while True:
        disponible = input("¿Está disponible? (s/n): ")

        if validar_disponible(disponible):
            break
        else:
            print("Debe ingresar s o n.")

    while True:
        try:
            stock = int(input("Ingrese stock: "))

            if validar_stock(stock):
                break
            else:
                print("El stock debe ser mayor o igual a 0.")

        except:
            print("Debe ingresar un número entero.")

    while True:
        try:
            vendidos = int(input("Ingrese vendidos: "))

            if validar_vendidos(vendidos):
                break
            else:
                print("Los vendidos deben ser mayor o igual a 0.")

        except ValueError:
            print("Debe ingresar un número entero.")

    agregado = agregar_producto(
        codigo,
        nombre,
        categoria,
        precio,
        disponible,
        stock,
        vendidos,
        productos,
        inventario
    )
    
    if agregado:
        print("Producto agregado correctamente.")
    else:
        print("No se pudo agregar el producto.")

def ejecutar_eliminar_producto(productos, inventario):
    codigo = input("Ingrese el código a eliminar: ")

    eliminado = eliminar_producto(productos, inventario, codigo)

    if eliminado:
        print("Producto eliminado.")
    else:
        print("El código no existe o ya fue eliminado.")

def ejecutar_programa():

    productos = {
        "P101": ["Cuaderno", "Papelería", 2490, True],
        "P102": ["Lápiz", "Papelería", 590, True],
        "P103": ["Botella", "Accesorios", 6990, False],
        "P104": ["Mochila", "Accesorios", 24990, True]
    }

    inventario = {
        "P101": [30, 15],
        "P102": [120, 50],
        "P103": [0, 10],
        "P104": [8, 25]
    }

    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Stock por categoría")
        print("2. Buscar productos por rango de precio")
        print("3. Actualizar precio")
        print("4. Agregar producto")
        print("5. Eliminar producto")
        print("6. Mostrar productos")
        print("7. Salir")
        print("===================================")

        opcion = leer_opcion()

        if opcion == 1:
            ejecutar_stock_categoria(productos, inventario)

        elif opcion == 2:
            ejecutar_busqueda_precio(productos, inventario)

        elif opcion == 3:
            ejecutar_actualizar_precio(productos)

        elif opcion == 4:
            ejecutar_agregar_productos(productos, inventario)

        elif opcion == 5:
            ejecutar_eliminar_producto(productos, inventario)

        elif opcion == 6:
            mostrar_producto(productos, inventario)

        elif opcion == 7:
            print("Programa finalizado.")
            break

ejecutar_programa()