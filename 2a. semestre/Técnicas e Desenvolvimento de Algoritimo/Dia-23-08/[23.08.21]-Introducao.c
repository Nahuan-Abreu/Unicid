#include <stdio.h> // importa a bibliote a basica da linguagem. Todos os comandos devem ser escito com letra minuscula.

// main é a funcao principal da linguagem, é obrigatorio ter uma para iniciar qualquer projeto. void = vazio.
int main(void){
  printf("Hello World\n"); //printf = mostra a mensagem na tela.
  printf("\nNome \tIdade \tCurso");
  printf("\nLuan \t20 \t\tADS");
  printf("\nEnzo \t18 \t\tRedes");// usamos o \n para pular uma linha, e o \t para dar um tab (4 espaços). para colocar aspas na tela ou colocar algo dentro de aspas colcomos o comando \" e \'para aspas simples.
  printf("\n\"Nahu\" \t17 \t\t\'ADS\'");
  printf("\nPara escrever a Bara usamos o comando \\ ");

  return 0; // encerra a funcao
}