package ListaExercicios;
import java.util.*;
public class exercicio5 {
	public static void main(String[] args) {
		double sm,salario,calculo;
		sm = 788.00;
				
		Scanner sc = new Scanner(System.in);
		System.out.println("Informa seu salário R$: ");
		salario = sc.nextFloat();
		calculo =  salario / sm;
		System.out.println("Você recebe " +calculo+ " salários mínimos");
		
		
	}
}
