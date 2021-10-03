/*
1) leia 2 notas de um aluno.
  Calcular e mostrar a média na tela.
  Informe se o aluno está aprovado, reprovado, exame.

  se a média >= 7   Aprovado
  se a média < 5    Reprovado  
  Entre 5 e 7       Exame

*/
#include <stdio.h>

int main(void) {
  float A, B, med;
  printf("Digite a primeira nota: ");
  scanf("%f",&A);
  printf("Digite a segunda nota: ");
  scanf("%f",&B);
  med = (A+B)/2;
  printf("Sua média é %.2f", med);
  
  if (med >= 7){
    printf("\nVocê está APROVADO");
  }else if (med < 5) {
    printf("\nVocê está REPROVADO");
  }else printf("\nVocê está EXAME");
  return 0;
}