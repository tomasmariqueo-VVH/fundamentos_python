#Variables y tipos de datos
#Tipo texto ('str')
nombre = "Camila"
ciudad = "Santiago"
print(nombre)
print(ciudad)
print(type(nombre))

"""
Debajo del ejemplo, crea tres variables con el nombre de una película, un videojuego y una asignatura. Muéstralas
con print() y aplica type() a una de ellas.
"""

nombre_pelicula = input("Ingrese nombre de la película: ")
nombre_videojuego = input("Ingrese nombre del videojuego: ")
nombre_asignatura = input("Ingrese nombre de la asignatura: ")
tipoVar = type(nombre_pelicula)

print(f"""Nombre de la pelicula: {nombre_pelicula}
Nombre del videojuego: {nombre_videojuego}
Nombre de la asignatura: {nombre_asignatura}
El tipo de texto es: {tipoVar}""")

#Tipo entero ('int')
edad = 16
cantidad = 25
print(edad)
print(cantidad)
print(type(edad))

"""
Crea variables numéricas para tu edad, cantidad de hermanos y año actual. Muestra las tres con print() y verifica el
tipo de una con type().
"""

miEdad = int(input("Ingrese su edad: "))
hermanos = int(input("Ingrese su cantidad de hermanos: "))
fechaActual = int(input("Ingrese la fecha actual: "))
tipoVar2 = type(miEdad)
print(f"""Mi edad: {miEdad}
Hermanos: {hermanos}
Fecha: {fechaActual}
Tipo de variable: {tipoVar2}""")

#Decimales ('float')
precio = 1599.90
altura = 1.65
print(precio)
print(altura)
print(type(altura))

"""
Declara variables para el precio de un producto, la temperatura y un promedio de notas. Imprime los tres valores y
utiliza type() en dos de ellos.
"""

precio = float(input("Inserte un precio: "))
temp = float(input("Inserte la temperatura: "))
promedio = float(input("Inserte un promedio: "))
print(f"""El precio del producto es: {precio}
La temperatura es: {temp}
El promedio de notas es: {promedio}""")
print(type(precio), type(temp), type(promedio))

#Booleanos ('bool')
tiene_computador = True
esta_lloviendo = False
print(tiene_computador)
print(esta_lloviendo)
print(type(tiene_computador))

"""
Crea tres variables booleanas para indicar si tienes Internet, si terminaste la tarea y si tienes clases mañana.
Imprime sus valores y verifica el tipo de una.
"""

tengoInternet = True
terminéLaTarea = False
tengoClaseMañana = True
print(f"""Tengo internet? {tengoInternet}
Terminé mi tarea? {terminéLaTarea}
Tengo clase mañana? {tengoClaseMañana}""")
print(f"Los tipos de variables son: {type(tengoInternet)}, {type(terminéLaTarea)}, {type(tengoClaseMañana)}")

"""
En el mismo archivo, agrega una ficha de producto que contenga nombre (str), cantidad (int), precio (float) y
disponibilidad (bool). Debes imprimir cada valor y comprobar su tipo.
"""

nombreProducto = 'Pan'
cantidadProducto = 12
valorProducto = 2000.5
estáDisponible = True
print(f"""Nombre del producto: {nombreProducto}, Tipo de variable: {type(nombreProducto)}
Cantidad del producto: {cantidadProducto}, Tipo de variable: {type(cantidadProducto)}
Valor del producto: {valorProducto}, Tipo de variable: {type(valorProducto)}
Está disponible? {estáDisponible}, Tipo de variable: {type(estáDisponible)}""")