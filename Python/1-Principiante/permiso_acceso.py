#Crea una función llamada permiso_acceso(edad, tiene_boleto, es_vip) que devuelva True o False (un booleano) indicando si una persona puede entrar a un evento.

#Reglas de acceso:Para entrar, la persona obligatoriamente debe ser mayor de edad (>= 18 años).
#Si es mayor de edad, entra solo si cumple una de estas dos condiciones: tiene boleto O es un invitado VIP.

# MI LÓGICA EN PAPEL
 
#Ejercicio típico de bucles y condicionales

#Como hack para optimización puede usar operadores
"""1. Con el operador and (Pon lo más falso primero)
Para que un and sea verdadero, todo tiene que ser verdadero. Si la primera condición es falsa, Python ya sabe que todo valió madre y no lee lo demás.

Mal optimizado: if funcion_pesada_que_tarda_un_minuto() and edad >= 18:
(Python siempre va a correr la función pesada primero).

Optimizado: if edad >= 18 and funcion_pesada_que_tarda_un_minuto():
(Si el usuario tiene 17 años, Python ve el False al inicio y jamás ejecuta la función pesada. Te ahorraste un minuto de procesamiento).

2. Con el operador or (Pon lo más seguro primero)
Para que un or sea verdadero, basta con que uno sea verdadero. En cuanto encuentra un True, se detiene.

Optimizado: if es_vip or revisar_historial_de_boletos_en_base_de_datos():
(Si es VIP, entra directo. Python ni se molesta en ir a buscar a la base de datos)."""



def permiso_acceso(edad, tiene_boleto, es_vip):
    #ocupamos la optimización del código para realizarlo en una sola línea
    #colocamos la condicional más pesada al inicio para que descarte de inmediato
    #En caso de que se cumpla continua con las otras condicionales
    return edad >= 18 and (tiene_boleto or es_vip)
    

print(permiso_acceso(18,True,True))