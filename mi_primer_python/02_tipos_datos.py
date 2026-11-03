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

miEdad = input("Ingrese su edad: ")
hermanos = input("Ingrese su cantidad de hermanos: ")
fechaActual = input("Ingrese la fecha actual: ")
tipoVar2 = type(miEdad)
print(f"""Mi edad: {miEdad}
Hermanos: {hermanos}
Fecha: {fechaActual}
Tipo de variable: {tipoVar2}""")