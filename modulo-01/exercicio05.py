#Implemente uma função recursiva que recebe um número inteiro 
# decimal e retorna sua representação binária como uma string.
#  Para realizar essa conversão, utilize o método de divisão 
# sucessiva, onde você divide o número decimal por 2 e coleta
#  os restos até que o quociente seja zero.
#  A ordem dos restos coletados, de baixo para cima, 
# forma o número binário correspondente.

def decimal_para_binario(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    
   
    return decimal_para_binario(n // 2) + str(n % 2)



print(decimal_para_binario(13)) 
