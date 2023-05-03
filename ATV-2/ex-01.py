folha = float(input('digit o numero de copias: '))
if(folha <= 100):   
     valor = folha * 0.25
     print("O valor a tota a ser pago é de R$ {}".format(valor))
else:
     valor = folha * 0.20
     print("O valor a tota a ser pago é de R$ {}".format(valor))
