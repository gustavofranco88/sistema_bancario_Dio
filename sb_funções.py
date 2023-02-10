# criar funçoes de: +saque, +depósito, +extrato, +criar_user, +criar_conta

def saque(*, saldo, valor, extrato, limite, num_saques, limite_saques):
    if limite_saques > 0:
        # saq = float(input('Digite o valor do saque '))
        if valor > saldo or valor == 0:
            print('Não é possivel sacar este valor')
            # op = int(input('Escolha uma opção '))
        elif valor > limite:
            print('escolha um valor de saque até 500')
            # op = int(input('Escolha uma opção '))
        else:
            saldo -= valor
            extrato.append(valor * (-1))
            limite_saques -= 1
            # op = int(input('Escolha uma opção '))
    else:
        print('Voce ja fez os 3 saques do dia')
        # op = int(input('Escolha uma opção '))

    return saldo, extrato


def deposito(saldo, valor, extrato):
    # dep = float(input('Digite o valor do depósito '))

    if valor > 0:
        saldo += valor
        extrato.append(valor)
        # op = int(input('Escolha uma opção '))
    else:
        print('Valor Invalido')
    return f'saldo= {saldo}, extrato= {extrato}'


def extrato(saldo, extrato):
    print('-' * 30)
    print('EXTRATO'.center(30))
    print('-' * 30)
    for i in extrato:
        if i > 0:
            print(f'--Depósito = R${i:.2f}'.replace('.', ','))
        else:
            print(f'--Saque = R${i:.2f}'.replace('.', ','))
    print(f'\n  SALDO = {saldo:.2f}'.replace('.', ','))
    print('-' * 30)
    print('*' * 30)


def new_user():
    user = dict()
    user['nome'] = str(input('Nome: '))
    user['cpf'] = str(input('CPF(Somente os numeros: '.replace('-' or '.', '')))
    if '.' in user['cpf']:
        user['cpf'] = user['cpf'].replace('.', '')
        if '-' in user['cpf']:
            user['cpf'] = int(user['cpf'].replace('-', ''))
    user['data_nascimento'] = str(input('Data de nascimento: '))
    logradouro = str(input('Logradouro: '))
    nro = str(input('Numero: '))
    bairro = str(input('Bairro: '))
    cidade = str(input('Cidade: '))
    sigla = str(input('UF: '))
    endereco = f'{logradouro.title()}, {nro} - {bairro.title()} - {cidade.title()}/{sigla.upper()}'
    user['endereço'] = endereco

    users = [user]
    return users


print(new_user())


# print(extrato(1000, extrato=[100, -456]))

# print(deposito(1000, 345, extrato=[]))


'''
s = 1000
valor = 300
extrato = []
limite = 500
num_saque = 0
lim_saque = 3

print(saque(
    saldo=s, valor=valor, extrato=extrato, limite=limite, num_saques=num_saque, limite_saques=lim_saque ))



#print(saque())
'''
