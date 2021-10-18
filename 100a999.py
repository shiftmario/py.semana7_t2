def numero(num):
    centena = int(num/100)
    dezena = int((num - centena*100)/10)
    unidade = int(num - (centena*100 + dezena*100))
    li = [centena,dezena,unidade]
    cont = 0
    for i in li:
        if i%2 == 0:
            cont += 1 
    
    print(f'\no número {num} tem {cont} digitos pares')

n = int(input('\ndigite um numero entre 100 e 999:'))
numero(n)