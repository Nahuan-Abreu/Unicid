package Setimaaula;
import java.util.*;
public class exercicio2 {
public static void main(String[] args) {
		
		int a,par=0;
		int[] vet1 = new int[10];
		Scanner sc = new Scanner(System.in);
		
		for(a=0;a<10;a++) {
			System.out.println("Digite um valor");
			vet1[a]=sc.nextInt();
		}
		
		
		for(a=0;a<10;a++) {
			
			System.out.println("resto da divisao " + vet1[a]%2);
			if((vet1[a]%2)==0) {
				par++;
				System.out.println(par);
			}	
		}
		
		System.out.println("Total de numeros pares =" + par);

	}
}
