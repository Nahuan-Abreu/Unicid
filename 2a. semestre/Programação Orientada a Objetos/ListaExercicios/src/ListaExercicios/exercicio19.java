package ListaExercicios;
import java.util.*;
public class exercicio19 {
	public static void main (String[]args) {
		int i,num[],fparte,nparte;
		Scanner sc = new Scanner(System.in);
		num = new int[10];
		fparte = 0;
		nparte = 0;
		System.out.println("Digite 10 números: ");
		
		for(i=0;i<10;i++) {
			num[i] = sc.nextInt();
		}for(i=0;i<10;i++){
			if(num[i]>=10 && num[i]<=20){
				fparte = fparte + 1;
			}else nparte = nparte+1;
		}
		
		System.out.println("Quantidade dos numeros que fazem parte do intervalo [10,20] são: "+fparte);
		System.out.println("Quantidade dos numeros que não faz parte do intervalo [10,20] são: "+nparte);

	}
}
