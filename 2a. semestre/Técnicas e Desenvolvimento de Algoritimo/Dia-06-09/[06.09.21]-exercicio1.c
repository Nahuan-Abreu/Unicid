/*
Operadores Relacionais
------------------------

>     maior 
>=    maior/igual
<     menor 
<=    menor/igual
==    igual (comparação)
!=    Diferente


OBS: Um sinal de = faz atribuição, dois sinais de igauis (==) faz uma comparação
Exemplo: med = 9 (isso e uma atribuicao, a variavel tem o valor de 9);
if (a==b) (É uma comparacao se a variavel a tem o mesmo valor que a variavel b, ou seja, ele esta fazendo uma comparacao.)
*/
//--------------------------------------------------------------------------
/*
1) Leia 2 notas de um aluno.
Calcular e mostrar a média na tela.
Informare se o aluno está aprovado ou reprovado, sabendo que a média para aprovacao é 6 (seis)
*/
/*
%d =  usamos quando usamos variaveis int.
%f = usando quando usamos variaveis float.
*/
#include <stdio.h>

int main(void) {
  float n1,n2,med;
  printf("Digite a primeira nota: ");
  scanf("%f",&n1);
  printf("Digite a segunda nota: ");
  scanf("%f",&n2);
  med = (n1+n2) / 2;
  printf("Sua nota foi: %.2f",med);

  if (med >= 6) printf("\nParabens, voce foi aprovado");
  else printf("\nInfezlimente, voce foi reprovado");
  return 0;
}