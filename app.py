import os
os.system("cls")

productos = {
"P101":["Cuaderno","Papelería",2490,True],
"P102":["Lápiz","Papelería",590,True],
"P103":["Botella","Accesorios",6990,False],
"P104":["Mochila","Accesorios",24990,True] 
}

inventario = { "P101":[30,15],
"P102":[120,50],
"P103":[0,10],
"P104":[8,25]
}

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
            if opcion not in [1,2,3,4,5,6,7]:
                return opcion
            else:
                print("Debe seleccionar una opción válida.")
        except ValueError:
            print("Debe ingresar un número de tipo entero.")

def validar_codigo(codigo):
    return codigo.strip() != "" and codigo.upper() not in productos

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

        if precio >= precio_min and precio <= precio_max and stock != 0:
            if codigo in productos:
                titulo = productos[codigo][0]
                resultados.sort(titulo + "--" + codigo)

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

def eliminar_producto(codigo, productos, inventario):
    codigo = codigo.upper()

    if buscar_codigo(productos, inventario, codigo):
        del productos[codigo]
        del inventario[codigo]
        return True
    
    return False

def mostrar_producto(productos, inventario):
    print("==== PRODUCTOS =====")
    print(productos)
    print(inventario)

def ejecutar_stock_categoria(productos, inventario):
    categoria = input("Ingrese categoría de producto: ")
    total = stock_categoria(categoria, productos, inventario)
    print(f"El total de stock es: {total}")
