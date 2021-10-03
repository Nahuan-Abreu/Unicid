package Setimaaula;

public class exemplo2 {
	public static void main(String[] args) {	
		int[] notas = new int[10];
		int i,presentes=0,ausentes=0;
		notas[0]=1;
		notas[1]=0;
		notas[2]=1;
		notas[5]=1;
		for(i=0;i<10;i++) {
		   if(notas[i]==1)
			   presentes++;
		   if(notas[i]==0)
			   ausentes++; 
		}
		System.out.println("Presentes = " + presentes);
		System.out.println("Ausentes = " + ausentes);
	}
}
