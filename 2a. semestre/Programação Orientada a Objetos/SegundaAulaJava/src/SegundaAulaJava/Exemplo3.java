package SegundaAulaJava;
import java.util.*;
public class Exemplo3 {
	public static void main(String[] args) {
		// TODO Auto-generated methond stubn
		
		// metodo de repeticao for (quando nos sabemos quantas vezes irá repetir) e o while quando nao sabemos.
		
		//int i;
		/*METODO DE REPETICAO FOR*/
		// ---1---- = i=1 executado uma vez quando o laço inicia. inicio do laco
		//---2---- = 1<=10 execultada a cada interação, ate que numero ele vai
		//---3---- = i=i+1 ou i++(para fazer o contrario usamos o i=i-1 ou i--) execultada a cada interação. coloar pra repetir adicionando mais 1.
		/*for (i=1;i<=50;i=i+2) {
			System.out.println("i= "+ i);
			System.out.println("passei aqui");
						
		}*/
		
//		int senha=123,cod;
//		// leitura
//		Scanner sc = new Scanner(System.in);
//		System.out.println("Digite a senha");
//		cod = sc.nextInt();
//		
//		while (cod!=senha) {
//			System.out.println("Digite a senha novamente");
//			cod = sc.nextInt();
//			
//		}
//		System.out.println("Senha correta");
		int senha=123, cod;
		Scanner sc = new Scanner(System.in);
		
	 	do {
	 		
	 		System.out.println("Digite a senha");
	 		cod = sc.nextInt();
	 		
	 	}while(cod!=senha);
	 	
	 	System.out.println("Senha correta");
	}
} 
	
	
