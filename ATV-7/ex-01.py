def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
        
def menu():
    n = int(input("Digite a quantidade da sequencia de fibonacci você quer: "))

    for val in range(1,n+1):
        print("{} ".format(fibo(val)),end='')
    
menu()