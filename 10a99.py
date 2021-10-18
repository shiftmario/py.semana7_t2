def numero(num):
    dezena = int(num/10)
    unidade = num - dezena*10
    if dezena%2 ==0 and unidade%2 ==0:
        print('\nNenhum digito é ímpar.')
    elif dezena%2 ==0 or unidade%2 ==0:
        print('\nApenas um dígito é ímpar.')
    else:
        print('\nOs dois dígitos são ímpares.')

n  = int(input('\nDigite um numero entre 10 e 99:'))
numero(n)