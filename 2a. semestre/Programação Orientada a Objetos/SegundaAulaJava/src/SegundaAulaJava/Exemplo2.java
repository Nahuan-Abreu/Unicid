package SegundaAulaJava;
import java.util.*;
public class Exemplo2 {
	public static void main (String[] args) {
		String nome;
		float alt,peso;
		
		Scanner sc = new Scanner (System.in);
		
		System.out.println("Digite o nome");
		nome = sc.nextLine();
		
		System.out.println("Digite a altura");
		alt = sc.nextFloat();
		
		System.out.println("Digite o peso ");
		peso =  sc.nextFloat();
		
		System.out.println("Nome= "+ nome);
		System.out.println("IMC= "+ (peso)/(alt*alt));
		
		
	}
	
}