#Q2
#Mudando apenas uma linha, altere o código 
#anterior para imprimir o intervalo invertido.

def intervalo (a, b):
    if a > b:
        print("Valores invalidos")     
    elif a == b:
        print(a, end = '')
    else:
        intervalo(a+1, b)
        print(a, end = '')
    

intervalo (1, 10)