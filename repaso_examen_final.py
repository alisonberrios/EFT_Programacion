import os 
os.system("cls")

#Para poder trabajar los productos de la lista, debemos almacenar la información detallada del producto, 
#y la llave para acceder a ellos es a través del código.
# Diccionario de productos.
productos = {
"P101":["Cuaderno","Papelería",2490,True],
"P102":["Lápiz","Papelería",590,True],
"P103":["Botella","Accesorios",6990,False],
"P104":["Mochila","Accesorios",24990,True]
}

#Diccionario del inventario.
#Al igual que la llave de productos, buscaremos el inventario de cada uno de ellos por medio del código.
inventario = {  
"P101":[30,15],
"P102":[120,50],
"P103":[0,10],
"P104":[8,25]
}

#Como primera función, vamos a crear nuestro menú principal e interfaz directa con el usuario,
#donde se podrá visualizar cada una de las opciones que ofrece el programa.
