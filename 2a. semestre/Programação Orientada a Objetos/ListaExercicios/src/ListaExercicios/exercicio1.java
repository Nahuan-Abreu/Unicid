package ListaExercicios;
import java.util.*;
public class exercicio1 {

	public static void main (String[] args) {
		int ano,mes,dias,anosD,mesD,total;
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Digite a sua idade em anos, meses e dias.");
		System.out.println("Anos: ");
		ano = sc.nextInt();
		System.out.println("Meses: ");
		mes = sc.nextInt();
		System.out.println("Dias: "); 
		dias = sc.nextInt();
				
		anosD = ano*365;
		mesD = mes*30;
		total = anosD + mesD+ dias;
		
		System.out.println("\nA sua idade em dias é de: " + total +" dias");
	}
	
}
