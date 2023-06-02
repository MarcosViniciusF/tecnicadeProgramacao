n = int(input("Digite um numero: "))
cont = n
f = 1
def fct(f):
    cont = n
    f = 1
    print('Calculando {}! = '.format(n), end="")
    while cont > 0:
        print('{}'.format(cont), end='')
        print(' X 'if cont > 1 else ' = ', end='')
        f *= cont
        cont -= 1
    print('{}'.format(f))


fct(n)
