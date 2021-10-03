package Setimaaula;
import java.util.*;
public class exemplo4 {
    public static void main(String[] args) {

        int[] a1 = new int[5];
        int j;
        Scanner sc = new Scanner(System.in);
        //leitura
        for(j=0;j<5;j++){
          System.out.println("Digite um valor");
          a1[j] = sc.nextInt();
        }

        System.out.println("=============\n");
        //impressao
        for(j=0;j<5;j++){
          System.out.println("a1 = " + a1[j]);
        }

        System.out.println("\n===Alterando====\n");
         //altera os conteudos
        for(j=0;j<5;j++){
           a1[j]=a1[j]*2;
        }
        //impressao
        for(j=0;j<5;j++){
          System.out.println("a1 = " + a1[j]);
        }
     }
}
