package ListaExercicios;
import java.util.*;
public class exercicio17 {
	  public static void main(String[] args) {
		  Scanner sc = new Scanner(System.in);
		  int recebe;
		              
		  System.out.print("Digite um número: ");
		  recebe = sc.nextInt(); 
		              
		 for(int x = recebe; x > 0; x--){ 
			 for(int y = recebe; y > 0; y--){ 
				 System.out.print("*");
			 }
			 	System.out.println();       
		  }
		 sc.close();


		  }
		

	}
	
