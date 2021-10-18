def ordenar(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        if num2 < num3:
            print(num1, num2, num3)
        else:
            print(num1, num3, num2)
    elif num2 < num3:
        print(num2,num3,num1)
    else:
        print(num3, num2,num1)

print('\nOs número digitados serão ordenados em ordem crescente.')
numero1 = int(input('\nDigite o primeior número:'))
numero2 = int(input('\nDigite o segundo número:'))
numero3 = int(input('\nDigite o terceiro número:'))

ordenar(numero1, numero2, numero3)