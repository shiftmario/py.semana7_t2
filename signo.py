def signo(d,m):
    if m == 3:
        if d in [21,22,23,24,25,26,27,28,29,30,31]:
            print('\nSeu signo é Áries')
        else:
            print('\nSeu signo é Peixes')
    if m == 4:
        if d in [20,21,22,23,24,25,26,27,28,29,30]:
            print('\nSeu signo é Touro')
        else:
            print('\nSeu signo é Áries')
    if m == 5:
        if d in [21,22,23,24,25,26,27,28,29,30,31]:
            print('\nSeu signo é Gêmeos')
        else:
            print('\nSeu signo é Touro')
    if m == 6:
        if d in [22,23,24,25,26,27,28,29,30]:
            print('\nSeu signo é Câncer')
        else:
            print('\nSeu signo é Gêmeos')
    if m == 7:
        if d in [23,24,25,26,27,28,29,30,31]:
            print('\nSeu signo é Leão')
        else:
            print('\nSeu signo é Câncer')
    if m == 8:
        if d in [23,24,25,26,27,28,29,30,30]:
            print('\nSeu signo é Virgem')
        else:
            print('\nSeu signo é Leão')
    if m == 9:
        if d in [23,24,25,26,27,28,29,30,31]:
            print('\nSeu signo é Libra')
        else:
            print('\nSeu signo é Vigem')
    if m == 10:
        if d in [23,24,25,26,27,28,29,30]:
            print('\nSeu signo é Escorpião')
        else:
            print('\nSeu signo é Libra')
    if m == 11:
        if d in [22,23,24,25,26,27,28,29,30,31]:
            print('\nSeu signo é Sargitário')
        else:
            print('\nSeu signo é Escorpião')
    if m == 12:
        if d in [22,23,24,25,26,27,28,29,30]:
            print('\nSeu signo é Capricónio')
        else:
            print('\nSeu signo é Sargitário')
    if m == 1:
        if d in [20,21,22,23,24,25,26,27,28,29,30,31]:
            print('\nSeu signo é Aquário')
        else:
            print('\nSeu signo é Capricórnio')
    if m == 2:
        if d in [19,20,21,22,23,24,25,26,27,28,29]:
            print('\nSeu signo é Peixes')
        else:
            print('\nSeu signo é Aquário')

dia = int(input('\nDigite o dia em que você nasceu:'))
mes = int(input('\nDigite o mês em que você nasceu:'))

signo(dia, mes)