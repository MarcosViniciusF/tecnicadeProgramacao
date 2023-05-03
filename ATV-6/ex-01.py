n = int(input("Determine o número elementos da lista: "))
i = 0
lista = []
while i < n:
  elemento = int(input("Digite os elementos da lista: "))
  i += 1
  lista.append(elemento)
print("O array digitado é: {}".format(lista))