#Escreva uma função recursiva que recebe
#  um inteiro n e verifica se n é um valor primo, ou seja, 
# se é divisível apenas por si mesmo e por 1.

def eh_primo(n, divisor=2):

    if n <= 1:
        return False  
    if divisor == n:
        return True   
    if n % divisor == 0:
        return False  

    # Chamada recursiva
    return eh_primo(n, divisor + 1)


print(eh_primo(7))  
print(eh_primo(10)) 
