package Setimaaula;
import java.util.*;
public class exercicio1 {
	public static void main(String[] args) {
		
		int[] vet1 = new int[5];
		int[] vet2 = new int[5];
		
		int j;
		Scanner sc = new Scanner(System.in);
		
		//leitura
		for(j=0;j<5;j++){
			System.out.println("Digite um valor");
			vet1[j] = sc.nextInt();
		}
		//copiando vet1 para vet2
		for(j=0;j<5;j++){
			 vet2[j]=vet1[j]; // faz a copia de vet1 para vet2
		}
		
		System.out.println("=============");
		
		//impressao
		for(j=0;j<5;j++){
			System.out.println("vet2 = " + vet2[j]);
		}
	}
	
}
