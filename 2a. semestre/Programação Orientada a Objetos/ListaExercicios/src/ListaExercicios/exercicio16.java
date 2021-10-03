package ListaExercicios;
import java.util.*;
public class exercicio16 {
	public static void main(String[]args) {
		double a,b,c;
		Scanner sc = new Scanner(System.in);
		System.out.println("Digite a medida do primeiro lado do triângulo: ");
		a = sc.nextDouble();
		System.out.println("Digite a medida do segundo lado do triângulo: ");
		b = sc.nextDouble();
		System.out.println("Digite a medida do terceiro lado do triângulo: ");
		c = sc.nextDouble();
		
		if ((a<b+c)&&(b<a+c)&&(c<a+b)){
			System.out.println("Existe triângulo\n");
		    if((a==b) && (b==c) && (c==a)){
		    	System.out.println("O triângulo é um Equilatero");
		    }else if((a==b) || (b==c) || (c==a)){
		    	System.out.println("O triângulo é Isósceles");
		    }else System.out.println("O triângulo é um Escaleno");

		  }else System.out.println("As medidas não formam um triângulo");
		
	}

}
