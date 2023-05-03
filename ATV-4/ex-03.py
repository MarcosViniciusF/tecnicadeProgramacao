n = int(input("Digite um numero: "))
res = 0


def num():
    res = n % 2
    if (res == 0):
        print("O numero {} é par".format(n))
    else:
        print("O numero {} é impar".format(n))


print(num(res))
