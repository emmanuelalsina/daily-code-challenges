//==============================================================================
        //ENUNCIADO: Crear la función elegible_beca(promedio, ingresos_familiares, es_atleta)
// que devuelva True o False si el alumno califica para el apoyo.

// REGLAS DEL NEGOCIO:
// 1. El promedio obligatorio debe ser mayor o igual a 8.5.
//2. Si lo cumple, se le da la beca si tiene ingresos menores a 10000 ó si es atleta.
//==============================================================================

// MI LÓGICA EN PAPEL (Escríbela aquí abajo en lenguaje humano/matemático antes de programar):

//Creamos la clase
//dentro de ella debemos crear un metodo que sirva como filtro , por medio de operadores, para saber si es elegible parala beca
//&& es and y el or || en java
//el PRIMER filtro es el promedio, si no se cumple Java descarta en automatico al postulado
// Si se cumple, entra el siguiente filtro:
// Ya sea que el postulado sea atleta o su ingreso sea menor a los 10000, será acreedor


//clase principal
public class ElegibleBeca {

    //metodo main
    //void significa: "Este metodo ejecuta una accion, pero no devuelve nada
    public static void main(String[] args) {
        System.out.println(filtro(8,9500,true));


    }

    //metodo filtro para saber si es elegible para la beca
    //boolean significa: "Este metodo va a calcular algo y te va a regresar un true o un false
    public static boolean filtro (double promedio,int ingresos_familiares, boolean es_atleta) {
        return promedio >= 8.5 && (ingresos_familiares > 10000 || es_atleta);

    }
}
