# ==============================================================================
# ENUNCIADO: Crear la función elegible_beca(promedio, ingresos_familiares, es_atleta)
# que devuelva True o False si el alumno califica para el apoyo.
#
# REGLAS DEL NEGOCIO:
# 1. El promedio obligatorio debe ser mayor o igual a 8.5.
# 2. Si lo cumple, se le da la beca si tiene ingresos menores a 10000 ó si es atleta.
# ==============================================================================

# MI LÓGICA EN PAPEL (Escríbela aquí abajo en lenguaje humano/matemático antes de programar):
#

def elegible_beca(promedio, ingresos_familiares, es_atleta):
    #aprovecha al 100% el cortocircuito lógico: 
    #si alguien viene con promedio de 7.0, Python lee la primera condición, da False y ni se molesta en mirar los ingresos ni si es atleta.
    return  promedio >= 8.5 and (ingresos_familiares < 10000 or es_atleta)
  

print(elegible_beca(8.5,9500,True))