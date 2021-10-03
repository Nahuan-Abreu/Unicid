/*
5) Ler 1 número float
Informar se o número é POSITIVO ou NEGATIVO.
Considere o n zero = positivo
*/
#include <stdio.h>

int main(void) {
  float num;
  printf("Digite um número: ");
  scanf("%f",&num);
  if (num >= 0) printf("O número digitado é positivo.");
  else printf("O número digitado é negativo");
  return 0;
}