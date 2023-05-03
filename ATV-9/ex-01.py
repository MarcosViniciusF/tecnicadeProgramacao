C = float(input('Digite o capital inicial: R$ '))
i = float(input('Digite a taxa de juros em porcentagem: '))
i = i / 100
t = int(input('Digite o prazo em meses da aplicação: '))
Ci = C
MT = 0
def calculo_juros ():
    if(t == 0):
        return C
    MT = C * (1 + i) ** t
    return MT

J = calculo_juros() - Ci
print('O montante após {} meses é = R$ {:.2f}' .format(t, calculo_juros()))
print ('O ganho com juros no final dos {} meses é = R$ {:.2f}' .format(t, round(J,2)))
