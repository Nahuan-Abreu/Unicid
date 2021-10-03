/*
2) Ler 2 números inteiros (A,B).
   Mostrar o maior número lido ou uma mensagem que os números são iguais
   --> o maior é A
   --> o menor é B
   --> os números são iguais
*/
#include <stdio.h>

int main(void) {
  int A,B;
  printf("Digite o primeiro número: ");
  scanf("%d",&A);
  printf("Digite o segundo número: ");
  scanf("%d",&B);
  if(A > B){
    printf("o maior é %d",A);
  }else if(B > A){
    printf("o maior é %d",B);
  }else printf("os números são iguais");
  
  return 0;
}