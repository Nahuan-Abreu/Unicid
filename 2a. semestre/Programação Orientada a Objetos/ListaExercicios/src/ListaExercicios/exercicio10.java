package ListaExercicios;
import java.util.*;
public class exercicio10 {
	public static void main (String[] args) {
	/*qtm = Qunatide de Ma�as*/
	double qtm,preco1,preco2;
	Scanner sc = new Scanner(System.in);
	System.out.println("Digite a quantidade(s) de ma�a(s): ");
	qtm =sc.nextDouble();
	preco1 = qtm * 0.30;
	preco2 = qtm * 0.25;
	if(qtm < 12 ){
		System.out.printf("O valor total da compra foi de R$:  %.2f ",preco1);
	}else{
		System.out.printf("O valor total da compra foi de R$: %.2f ",preco2);
		}			
	}
}
