
//Enunciado: Crear función contar_patas(pollos, vacas, cerdos) que devuelva el total de patas en la granja.
        //Pollos = 2 patas, Vacas = 4 patas, Cerdos = 4 patas.


//creamos una funcion con las variables pollos, vacas, cerdos
//dentro de esa funcion se tiene que hacer la operacion:
        //de multiplicar el numero que se pase en el parámetro por el número de patas

//clase
public class ContadorPatas{

    //metodo main
    public static void main(String[] args) {

        System.out.println(contador(3,3,3));


    }

    //metodo ContadorPatas
    public static int contador (int pollo, int vaca, int cerdo) {

        return pollo * 2 + vaca * 4 + cerdo * 4 ;

    }



}



