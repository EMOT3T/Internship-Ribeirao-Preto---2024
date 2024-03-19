#include <iostream>
#include <stdio.h>

int indice=13, soma=0, k=0;

int main() {
    
    while(k<indice){
        k+=1;
        soma+=k;
    }
    
    printf("%d", soma);
    
}

// Output is: 91