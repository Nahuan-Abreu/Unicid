package SextaaAula;
import java.util.*;
public class exemplo1 {
	public static void main (String[] args) {
		int op;
		Scanner sc = new Scanner(System.in);
	while(true) {
		System.out.println("1-opcao");
		System.out.println("2-opcao");
		System.out.println("3-sair");
	
		op = sc.nextInt();
		switch (op) {
		case 1:
			System.out.println("Opcao 1");
			break;
		case 2:
			System.out.println("Opcao 2");
			break;
		case 3:
			System.out.println("Saiu");
			System.exit(0);
			break;
		default:
			System.out.println("Opcao errada");
			}
		}
	}
}
