/*
2) Ler DOIS números inteiros.
    Iformar se os números lidos são IGUAIS ou DIFERENTES
*/
#include<stdio.h>
int main (void){
    int n1,n2;
    printf("Digite um número: ");
    scanf("%d",&n1);
    printf("Digite o segundo numero: ");
    scanf("%d",&n2);

    if (n1 == n2) printf("Os numeros sai iguais");
    else printf("Os numeros nao sao iguais");
    
}
