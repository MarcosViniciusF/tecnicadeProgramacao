#include <stdio.h>
#include <stdlib.h>

int main ( void ) {
int a[10], i;
float soma = 0;
float media;

for ( i = 0; i < 10; i++ ) {
printf ( "Digite a nota %d: ", i + 1, i + 1 );
scanf ( "%d", &a[i] );
}

for ( i = 0; i < 10; i++ )
printf ( "\nNota %d : %d\n",i +1, a[i] );

for ( i = 0; i < 10; i++ )
soma += a[i];
printf ( "\nSoma total: %.2f\n", soma );

media = soma / 10;
printf ( "\nMedia : %.2f\n", media );

system ("pause");

return 0;
}