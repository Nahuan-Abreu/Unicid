package ListaExercicios;
import java.util.*;
public class exercicios3 {
	public static void main(String[] args) {
		/*sr = saldo reajustado.*/
		Double saldo,sr;
		Scanner sc = new Scanner(System.in);
		System.out.println("Digite o seu saldo: R$ ");
		saldo = sc.nextDouble();
		sr = saldo * 1.01;
		System.out.println("O seu saldo reajusatado com 1% é de R$ " + sr);
	}
}

