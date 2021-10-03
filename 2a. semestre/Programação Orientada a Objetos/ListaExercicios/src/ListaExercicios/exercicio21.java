package ListaExercicios;
import java.util.*;
public class exercicio21 {
	  public static void main(String[] args) {
		// TODO Auto-generated method stub
		                Scanner dado = new Scanner(System.in);
		                int conth = 0,contf200 = 0,maior = 0,menor = 200,idade,menorsalidade = 0;
		                double salario = 1,menorsalario = 9999,ssalario = 0;
		                char sexo,menorsalsexo = 0;
		                while (salario > 0){
		                System.out.println("Qual a idade do entrevistado: ");
		                idade = dado.nextInt();
		                System.out.println("Sexo<M/F>: ");
		                sexo = dado.next().charAt(0);
		                System.out.println("Salario: R$");
		                salario = dado.nextDouble();

		                if(salario > 0 ){

		                ssalario = ssalario + salario;
		                conth = conth +1;
		                }
		                if(idade > maior){
		                maior =idade;
		                }
		                if(idade < menor){
		                menor = idade;

		                }
		                if(salario <= 200 && sexo =='f'){
		                contf200 =contf200 + 1;
		                }
		                if(salario < menorsalario){
		                        menorsalario = salario;
		                        menorsalidade = idade;
		                        menorsalsexo = sexo;
		                }
		                if(idade < 0){
		                System.out.println("Media dos salarios do grupo: R$"+ssalario/conth);
		                System.out.println("Menor idade: "+menor+" anos");
		                System.out.println("Maior idade: "+maior+" anos");
		                System.out.println("A quantidade de mulheres com salário até R$ 200,00 foi de: "+contf200);
		                System.out.println("A idade da pessoa e o sexo que possui o menor salário "+menorsalario+" foi da pessoa com idade "+menorsalidade+" do sexo "+menorsalsexo);
		                }
		        }
		                dado.close();

		  }
		}


