package ListaExercicios;
import java.util.*;
public class exercicio16 {
	public static void main(String[]args) {
		double a,b,c;
		Scanner sc = new Scanner(System.in);
		System.out.println("Digite a medida do primeiro lado do tri�ngulo: ");
		a = sc.nextDouble();
		System.out.println("Digite a medida do segundo lado do tri�ngulo: ");
		b = sc.nextDouble();
		System.out.println("Digite a medida do terceiro lado do tri�ngulo: ");
		c = sc.nextDouble();
		
		if ((a<b+c)&&(b<a+c)&&(c<a+b)){
			System.out.println("Existe tri�ngulo\n");
		    if((a==b) && (b==c) && (c==a)){
		    	System.out.println("O tri�ngulo � um Equilatero");
		    }else if((a==b) || (b==c) || (c==a)){
		    	System.out.println("O tri�ngulo � Is�sceles");
		    }else System.out.println("O tri�ngulo � um Escaleno");

		  }else System.out.println("As medidas n�o formam um tri�ngulo");
		
	}

}
