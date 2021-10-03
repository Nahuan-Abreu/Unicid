/*
3) Ler 1 número float
   Informar se o número lido é:
   -> positivo
   -> negativo
   -> nulo
*/

#include <stdio.h>

int main(void) {
  float n;
  printf("Digite um número: ");
  scanf("%f",&n);
  if(n >0){
    printf("O número é positivo");

  }else if(n < 0){
    printf("O número é negativo");
  }else printf("Este número e nulo");
  return 0;
}