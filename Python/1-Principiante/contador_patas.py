
#Enunciado: Crear función contar_patas(pollos, vacas, cerdos) que devuelva el total de patas en la granja.
#Pollos = 2 patas, Vacas = 4 patas, Cerdos = 4 patas.


#creamos una funcion con las variables pollos, vacas, cerdos
#dentro de esa funcion se tiene que hacer la operacion:
#de multiplicar el numero que se pase en el parámetro por el número de patas

def contar_patas(pollo, vaca, cerdo):
 
    return (pollo * 2 ) + (vaca * 4) + (cerdo * 4)

print(contar_patas(3,3,3))
