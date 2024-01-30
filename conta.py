def multiplicar(n1,n2):
    contador = 0
    resultado = 0
    while contador < n2:
        resultado += n1
        contador += 1
        
    print("O resultado é: ", resultado)
    


n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
multiplicar(n1,n2)
