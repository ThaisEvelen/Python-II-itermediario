#Q1.
#Faça um procedimento recursivo que receba dois valores inteiros a e b e 
#imprime o intervalo fechado entre eles. Se a > b imprima uma mensagem de erro.

a = int(input("Digite um valor:"))
b = int(input("Digite um valor maior que o anterior:"))

def intervalo (a, b):
    if (a > b):
        print("Valores invalidos")     
    elif(a == b):
        print("Caso base")
        return a
    else:
        print(f'{b-a}')
        return (b-a)
print(f'A sequencia numérica é {b-a}')
