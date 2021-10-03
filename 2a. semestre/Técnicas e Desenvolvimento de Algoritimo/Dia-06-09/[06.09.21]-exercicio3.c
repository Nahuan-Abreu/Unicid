/*
3) Ler DOIS números inteiros e mostre o maior numero lido na tela (ignore a condicao de numeros iguais).

*/
#include <stdio.h>

int main(void) {
  int n1,n2;
  printf("Digite o primeiro numero: ");
  scanf("%d",&n1);
  printf("Digite o segundo numero: ");
  scanf("%d",&n2);
  if (n1 > n2) printf("O primeiro numero e maior: %d", n1);
  else printf("O segundo numero e maior: %d",n2);
  return 0;
}