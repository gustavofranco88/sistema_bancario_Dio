from funções_do_banco import *

saldo = 1000.00
limite_saque = 500
num_saque = 3
movimentacoes = []
usuarios = []
numero_conta = 1
contas = []

print('*' * 30)
print('BEM VINDO AO BANCO DIO'.center(30))
print('*' * 30)
menu()
escolha = int(input('Digite sua opção: '))
while True:
    if escolha == 1:
        valor = float(input('Digite o valor do deposito: '))
        if valor > 0:
            saldo = deposito(saldo, valor, movimentacoes)
            escolha = int(input('Digite sua opção: '))
        else:
            print('Valor invalido, deve ser maior que 0')
            escolha = int(input('Digite sua opção: '))
    elif escolha == 2:
        if num_saque > 0:
            valor = float(input('Digite o valor do saque: '))
            saldo, num_saque = saque(
                saldo=saldo,
                valor=valor,
                num_saques=num_saque,
                limite_saque=limite_saque,
                movimentacoes=movimentacoes
            )
            escolha = int(input('Digite sua opção: '))
        else:
            print('Voce ja fez os 3 saques do dia')
            escolha = int(input('Digite sua opção: '))

    elif escolha == 3:
        extrato(saldo, movimentacoes=movimentacoes)
        escolha = int(input('Digite sua opção: '))

    elif escolha == 4:
        criar_usuario(usuarios)
        escolha = int(input('Digite sua opção: '))

    elif escolha == 5:
        agencia = '0001'

        conta = (criar_conta(agencia, numero_conta, usuarios))

        if conta != None:
            contas.append(conta)
            numero_conta += 1
        print(contas)
        escolha = int(input('Digite sua opção: '))

    elif escolha == 6:
        print(lista_contas(contas))
        escolha = int(input('Escolha sua opção: '))

    elif escolha == 17:
        print('Saindo')
        break
    else:
        print('Opção invalida')
        escolha = int(input('Escolha sua opção: '))

