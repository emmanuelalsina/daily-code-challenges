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
# MI LÓGICA EN PAPEL:
# Primero necesitamos input para que el usuario pueda colocar los minutos, lo podemos guardar en la variable minutos
# creamos una variable segundos para guardar dentro de ella la operacion que transforma min a seg
# creamos una funcion y le pasamos el parametro la variable 
#dentro de la funcion ejecutamos la c¿variable que hace la conversion
#retornamos el resultado a la variable seg
# mostramos el resultado en pantalla con f- strng para darle mas experiencia de usuario.
#podemos hacer lo mismo con el inicio del programa




def convert(min):
    seg = int(min * 60)

    return seg


print(convert(5))
print(convert(3))
print(convert(2))

