menu = (1, 2, 3, 4)
saldo = 0
limite_saque = 500
extrato =[]
saque = 3
print('*'*30)
print('BEM VINDO AO BANCO DIO'.center(30))
print('*'*30)
print('  MENU  '.center(30))
print('*'*30)
print('1 - Depósito')
print('2 - Saque')
print('3 - Extrato')
print('4 - Sair')
print('*'*30)
op = int(input('Escolha uma opção '))
while True:
    if op not in menu:
        op = int(input(f'Opção invalida, escolha uma opção do menu {menu} : '))
    if op == 1:
        dep = float(input('Digite o valor do depósito '))

        if dep > 0:
            saldo += dep
            extrato.append(dep)
            op = int(input('Escolha uma opção '))
        else:
            print('Valor Invalido')
    elif op == 2:
        if saque > 0:
            saq = float(input('Digite o valor do saque '))
            if saq > saldo or saq == 0:
                print('Não é possivel sacar este valor')
                op = int(input('Escolha uma opção '))
            elif saq > limite_saque:
                print('escolha um valor de saque até 500')
                op = int(input('Escolha uma opção '))
            else:
                saldo -= saq
                extrato.append(saq * (-1))
                saque -=1
                op = int(input('Escolha uma opção '))
        else:
            print('Voce ja fez os 3 saques do dia')
            op = int(input('Escolha uma opção '))
    elif op == 3:
        print('-'*30)
        print('EXTRATO'.center(30))
        print('-' * 30)
        for i in extrato:
            if i > 0:
                print(f'--Depósito = R${i:.2f}'.replace('.', ','))
            else:
                print(f'--Saque = R${i:.2f}'.replace('.', ','))
        print(f'\n  SALDO = {saldo:.2f}'.replace('.', ','))
        print('-' * 30)
        print('*'*30)


        op = int(input('Escolha uma opção '))

    else:
        print('Saindo')
        break
