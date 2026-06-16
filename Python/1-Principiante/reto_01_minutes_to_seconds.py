# Reto 1 - Principiante
# Fuente: Edabit
# Fecha: [08.06.2026]
#
# ENUNCIADO:
# Crea una función que convierta minutos a segundos.
#
# EJEMPLOS:
# convert(5)  --> 300
# convert(3)  --> 180
# convert(2)  --> 120
#
# REGLAS:
# - El parámetro siempre será un número entero positivo
# - Devuelve el resultado como número entero
#
# MI LÓGICA EN PAPEL

# creamos una funcion llamada "convert" cuyo parametro sera la cantidad de minutos que se requieran para hacer la conversión a segundos
#retornamos el resultado del parámetro multplicado por 60 (1 min = 60 seg)




def convert(min):
    return int(min * 60)


print(convert(5))
print(convert(3))
print(convert(2))

