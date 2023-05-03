valor = float(input("Informe o valor da compra: "))
des = float(input("Informe o pecentual deve ser um valor entre 0 e 1: "))
novoValor = valor * (des / 100)
print(" o valor com desconto é de R${}".format(novoValor))