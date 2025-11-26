#Q1.
#Faça um procedimento recursivo que receba dois valores inteiros a e b e 
#imprime o intervalo fechado entre eles. Se a > b imprima uma mensagem de erro.


def intervalo (a, b):
    if a > b:
        print("Valores invalidos")     
    elif a == b:
        print(a, end = '')
    else:
        print(a, end = '')
        intervalo(a+1, b)

intervalo (1, 10)