package ListaExercicios;
import java.util.*;
public class exercicio12 {
	public static void main(String[]args) {
		double altura,peso,masculino, feminino;
		int sexo;
		Scanner sc = new Scanner(System.in);
		System.out.println("Iforme a sua altura: ");
		altura = sc.nextDouble();
		System.out.println("Iforme o se peso: ");
		peso = sc.nextDouble();
		
		System.out.println("Esolha seu sexo:");
		System.out.println("1 - Feminino");
		System.out.println("2 - Masculino");
		sexo = sc.nextInt();
		masculino = (72.7*altura) - 58;
		feminino = (62.1*altura) - 44.7;
		switch (sexo) {
		case 1:
			System.out.printf("Seu peso ideal é de: %.2f ",feminino);
			break;
		case 2:
			System.out.printf("Seu peso ideal é de: %.2f",masculino);
			break;
		}
		
	}
	
}
