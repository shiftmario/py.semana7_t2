def estado_civil(name,num):
    if num == 1:
        nome_con = str(input('Digite o nome do seu cônjuge:')).strip()
        print(f'Número de Carcteres no nome {name} é {len(name)}')
        print(f'Número de Carcteres no nome {nome_con} é {len(nome_con)}')
    else:
        print(f'Número de Carcteres no nome {name} é {len(name)}')


nome = str(input('\nDigite seu nome:')).strip()
print('1 - casado\n2 - solteiro')
estado = int(input('\nQual seu estado civil atual:'))

estado_civil(nome,estado)