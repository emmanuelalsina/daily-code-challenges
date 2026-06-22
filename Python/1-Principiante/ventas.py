# Reto 1 - Semana 2 - Principiante+
# Fuente: Propio
# Fecha: [Semana 2]
#
# ENUNCIADO:
# Una tienda quiere analizar las ventas realizadas durante el día.
#
# Crea un programa que reciba una lista con los montos de las ventas
# y determine cuántas ventas fueron consideradas "ventas altas".
#
#
# EJEMPLOS:
#
# [150, 300, 50, 800, 200] --> 2
#
# [100, 90, 70] --> 0
#
# [1000, 500, 250] --> 3
#
#
# REGLAS:
#
# - Una venta es considerada alta si es mayor o igual a 250.
# - Los valores siempre serán números positivos.
# - Debes devolver únicamente la cantidad de ventas altas.
#
#
# MI LÓGICA EN PAPEL
#
# (Explica aquí los pasos en lenguaje humano antes de escribir código)
#¿Cuál es el problema real?   Necesito procesar una lista de datos, que itere sobre estos mismos y que devuelva las que cumplen una carácteristica en común

#¿Qué información entra?    una lista de numeros (en este caso montos de cuentas)

#¿Qué información debe salir?  el número de elementos (montos) que cumplan la  característica


#Plan: 
#crear una funcion que como parámetro reciba la lista de montos 

#Dentro de la función, ésta deberá iterar sobre cada elemnto de dicha lista y comparar el monto con el monto mpinimo
#si lo excede entonces lo agrega a otra lista y se guarda

#al final debe mostrar el numero de elemntos que cumplian la condición, en otras palabras el largo de la lista.


ventas_semanales = [200,500,100,230,600,250]
ventas_mensuales = [2000,7000,5000,15000]
def ventas (montos):
    high_sales = []
    for m in montos:
        if m >= 250:
            high_sales.append(m)
                
    return len(high_sales)

#Para poder visualizarlo Guardamos el resultado que escupe la función en una variable
#Oye, ejecuta el aparato ventas, y métete en su hueco estas pilas reales llamadas ventas_semanales, ventas_mensuales
result = ventas (ventas_semanales) 
result2 = ventas (ventas_mensuales)   

#lo imprimimos
print(result)

print(result2)