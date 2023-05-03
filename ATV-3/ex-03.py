numQuanti = int(input("Digite a quantidadede alunos: "))
cont = 0
somaNota = 0
while cont < numQuanti :
    notaAluno = float(input("Digite o nota do aluno [%d]: " %(cont+ 1)))
    cont = cont + 1
    somaNota = somaNota + notaAluno

media = somaNota  / numQuanti
print("A media da nota de {} alunos, é de {}".format(numQuanti, media))