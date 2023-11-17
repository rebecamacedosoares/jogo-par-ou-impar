def calcularParImpar(num1,num2):
    num1 = num1
    num2 = num2
    soma = num1 + num2
    result = soma%2
    parImpar = ''
    if result == 0:
        parImpar = 'par'
    elif result == 1:
        parImpar = 'impar'

    return parImpar