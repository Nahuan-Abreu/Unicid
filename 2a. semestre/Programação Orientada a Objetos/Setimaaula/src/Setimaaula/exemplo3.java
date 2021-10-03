package Setimaaula;
import java.util.*;
public class exemplo3 {

	public static void main(String[] args) {
		
		int[] num = new int[10];
		int i;
		Scanner sc = new Scanner(System.in);
		
		// leitura do dados para o array
		for(i=0;i<10;i++){
			System.out.println("Digite um número: ");
			num[i] = sc.nextInt();
		}
		
		// impressao dos dados contidos no array
		for(i=0;i<10;i++){
					System.out.println("num = " + num[i]);
		}
		
	}

}