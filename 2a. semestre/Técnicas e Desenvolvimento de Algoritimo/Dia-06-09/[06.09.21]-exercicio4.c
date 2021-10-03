/*
4) Ler 2 números inteiros.
Mostrar os números lidos em ordem CRESCENTE.

*/
#include <stdio.h>

int main(void) {
  int n1,n2;
  printf("Digite o primeiro número: ");
  scanf("%d",&n1);
  printf("Digite o segundo número: ");
  scanf("%d",&n2);
  if (n1 < n2) printf("\n Ordem crescente é %d e %d", n1,n2);
  else         printf("\n Ordem crescente é %d e %d", n2,n1);

  return 0;
}