// ==============================================================================
// Reto 1 - Principiante
// Fuente: Edabit
//
// ENUNCIADO:
// Crea una función que convierta minutos a segundos.
//
// REGLAS EN JAVA:
// - El parámetro de entrada debe tener un tipo de dato explícito.
// - La función debe declarar el tipo de dato que va a retornar.
// - Todo debe vivir dentro de una clase llamada: ConvertirMinutos
// ==============================================================================

// en Java se le llama metodo a lo que en python llamamos funcion


// TU CÓDIGO VA AQUÍ ABAJO:

public class ConvertirMinutos {


    // REGLA DE ORO: En Java, los métodos NO se pueden anidar (ninguno vive dentro de otro).
    // El metodo 'main' y tu metodo personalizado van al mismo nivel, como hermanos.

    // MOTOR DE ARRANQUE: La puerta de entrada obligatoria para que el programa ejecute.
    // Aquí es donde pruebas tu código. Lo que en Python iba suelto al final del archivo, aquí va adentro de main.
    public static void main(String[] args) {

        System.out.println(convert(5));
        System.out.println(convert(3));
        System.out.println(convert(2));


    }
    // ==============================================================================
    // CONFIGURACIÓN DEL METODO:
    // 1. El primer 'int' (después de static) le dice a Java: "Este método va a regresar un entero".
    // 2. El 'int minutos' dentro del paréntesis indica qué tipo de dato será el parámetro.
    // RULE: La primera vez que usas una variable, debes decir qué tipo es (como presentar a alguien nuevo).
    // ==============================================================================
    public static int convert (int minutos ) {
        // LÓGICA: Aquí ya no declaras el tipo de 'minutos' porque Java ya lo conoce.
        return  minutos * 60 ;
    }
}

