n1 = int(input("informe o primeiro numero: "))
n2 = int(input("informe o segundo numero: "))

def mdc(a, b):
    if b == 0:
        return a
    resto = a % b
    a = b
    b = resto
    return mdc(a, b)  
    
print("O MDC entre {} e {} é de {}".format(n1,n2,mdc(n1, n2))) 