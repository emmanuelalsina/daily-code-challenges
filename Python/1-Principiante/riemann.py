#   1. VALIDACIÓN DE ENTRADAS 

# Punto inicial (a >= 0 porque la función incluye raíz cuadrada)
while True:
    try:
        a = float(input("Por favor ingresa el punto inicial: "))
        if a >= 0:
            break
        else:
            print("Error: El número debe ser estrictamente mayor o igual que 0.")
    except ValueError:
        print("Error: Por favor, ingresa un valor numérico válido.")

# Punto final (debe ser mayor que 'a' para que el intervalo tenga ancho positivo)
while True:
    try:
        b = float(input("Por favor ingresa el punto final: "))
        if b > a:
            break
        else:
            print("Error: El número debe ser estrictamente mayor que el numero inicial.")
    except ValueError:
        print("Error: Por favor, ingresa un valor numérico válido.")

# Cantidad de rectángulos (entero positivo para evitar división entre cero)
while True:
    try:
        n = int(input("Por favor ingresa el número de rectángulos que usarás: "))
        if n > 0:
            break
        else:
            print("Error: El número debe ser estrictamente mayor que 0.")
    except ValueError:
        print("Error: Por favor, ingresa un valor numérico válido.")

# Método de evaluación de altura (normalizamos espacios y mayúsculas)
while True:
    t = input("¿Desde que lado quieres medir la altura: izquierda, derecha o centro? ").strip().lower()
    if t in ("izquierda", "derecha", "centro"):
        break
    else:
        print("Error: Por favor, ingresa una opción válida.")


#   2.  PREPARACIÓN DE VARIABLES 

base = (b - a) / n   # Ancho uniforme de cada rectángulo
area_total = 0       # Acumulador de áreas
izq = a              # Límite izquierdo del primer rectángulo, su valor empieza con el punto inicial
                    #posteriormente va cambiando cada vuelta


#  3.  CÁLCULO DE LA SUMA DE RIEMANN 

for i in range(n):
    der = izq + base  # Límite derecho del rectángulo actual

    # Definimos el punto 'x' donde se evaluará la altura según el método elegido
    if t == "izquierda":
        x = float(izq)
    elif t == "derecha":
        x = float(der)
    else:
        x = (izq + der) / 2

    # Evaluamos f(x) = 5x^2 + 3x - 7√x
    altura = 5 * (x ** 2) + 3 * x - 7 * (x ** 0.5)
    #formula básica para sacar área de un rectángulo 
    area_rectangulo = base * altura
    # sumamos el área del rectángulo al area total en cada vuelta
    area_total += area_rectangulo

    # Avanzamos el límite izquierdo para la siguiente iteración
    # cada que inicie la vuelta ahora el borde izquier toma el valor del derecho y es como se va recorriendo
    izq = der


#  4. RESULTADO FINAL 

print(area_total)


