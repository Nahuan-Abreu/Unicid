/*

6) Ler dois floats 
  Mostrar a soma, subtracao, multiplicacao e divisao.

*/
#include <stdio.h>

int main(void) {
  float A, B;
  printf("Digite o primeiro numero: ");
  scanf("%f",&A);
  printf("Digite o segundo numero: ");
  scanf("%f",&B);

  printf("\nA soma é ----------------->%.2f",A+B);
  printf("\nA subtracao é ------------>%.2f",A-B);
  printf("\nA multiplicacao é -------->%.2f",A*B);
  
  if (B == 0) printf("\nNão podemos divider por zero");
  else printf("\nA divisao é -------------->%.2f",A/B );
  return 0;
}