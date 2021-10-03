/*
4) Ler peso e altura de uma pessoa.
   Calcular o IMC e mostrar na tela.
   IMC = peso/ altura² 
   IMC = peso / (altura * altura)

*/
#include <stdio.h>

int main(void) {
  float peso,altura,imc;
  printf("Qual é o seu peso: ");
  scanf("%f",&peso);
  printf("Qual é a sua altura: ");
  scanf("%f",&altura);
  imc = peso / (altura * altura);
  if(imc <= 18.5){
    printf("Você está Magro");
  }else if(imc <= 25){
    printf("Você está no peso ideal");
  }else if(imc <= 30){
    printf("Você está sobrepeso");
  }else printf("Você está obeso");
  return 0;
}