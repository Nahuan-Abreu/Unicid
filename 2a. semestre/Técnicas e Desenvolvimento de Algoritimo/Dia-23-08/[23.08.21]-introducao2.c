#include <stdio.h>

int main(void){
  int teste, aux;
  teste = 6;
  aux = 15;

  printf("\nO valor da variável teste é %d", teste); // para colocar a varial dentro de uma string usamos a %d que vai ser substituido pelo valor da variavel.
  printf("\n%d é o valor da variável teste", teste);
  printf("\nOs valores das variáveis são %d e %d", teste, aux); // sempre colocamos nas ordem que queremos que aparecem as variaveis.

  return 0;
}