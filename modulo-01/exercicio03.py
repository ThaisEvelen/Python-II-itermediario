#Q3
#Escreva uma função recursiva que recebe um inteiro 
# n > 1 e calcula a soma dos valores entre n e 1.

def somatorio(n):
    if n == 1:
        return n
    else:
      return  n + somatorio(n-1)

print(somatorio(5))