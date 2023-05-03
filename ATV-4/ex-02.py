n = int(input("Digite um numero: "))
d = 0


def dias(d):
    d = n
    if (d == 1):
        print("Domingo")
    elif (d == 2):
        print("Segunda-feira")
    elif (d == 3):
        print("Terça-feira")
    elif (d == 4):
        print("Quarta-feira")
    elif (d == 5):
        print("Quinta-feira")
    elif (d == 6):
        print("Sexta-feira")
    elif (d == 7):
        print("Sábado")
    else:
        {
            print("Opção invalida!!!")
        }


print(dias(n))
