num = int(input("Digit um numero inteiro positivo: "))
while num !=0:
  restoDivisao = num % 10
  num = num // 10
  print(restoDivisao)
  