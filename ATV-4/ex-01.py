import time
n =  int(input("Digite um numero: "))

def contagem (x):
    x = n
    while x >= 0:
        print(x)
        time.sleep(0.5)
        x -= 1

print(contagem(n))
