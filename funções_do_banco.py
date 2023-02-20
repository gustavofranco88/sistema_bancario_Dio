# criar funçoes de: +saque, +depósito, +extrato, +criar_user, +criar_conta

saldo = 1000.00
limite_saque = 500
num_saque = 3
movimentacoes = []


def saque(*, saldo, valor, num_saques, limite_saque, movimentacoes):
    '''print(f'valor {type(valor)}')
    print(f'saldo {type(saldo)}')
    print(saldo)'''
    if valor > saldo or valor == 0:
        print('Não é possivel sacar este valor')
        print(f'Saldo não alterado, Seu saldo atual é R${saldo:.2f}'.replace('.', ','))
        print(f'saldo {type(saldo)}')
        # escolha = int(input('Digite sua opção: '))
    elif valor > limite_saque:
        print('escolha um valor de saque até 500')
        print(f'Saldo não alterado, Seu saldo atual é R${saldo:.2f}'.replace('.', ','))
        # escolha = int(input('Digite sua opção: '))
    else:
        saldo -= valor
        movimentacoes.append(valor * (-1))
        num_saques -= 1
        # escolha = int(input('Digite sua opção: '))
    return saldo


def deposito(saldo, valor, movimentacoes):
    # dep = float(input('Digite o valor do depósito '))

    if valor > 0:
        saldo += valor
        movimentacoes.append(valor)
    else:
        print('Valor Invalido')
    return saldo
    #return f'saldo= {saldo}, extrato= {extrato}'


def extrato(saldo, movimentacoes):
    print('-' * 30)
    print('EXTRATO'.center(30))
    print('-' * 30)
    for i in movimentacoes:
        if i > 0:
            print(f'--Depósito = R${i:.2f}'.replace('.', ','))
        else:
            print(f'--Saque = R${i:.2f}'.replace('.', ','))
    print(f'\n  SALDO = {saldo:.2f}'.replace('.', ','))
    print('-' * 30)
    print('*' * 30)
    return movimentacoes


def new_user():
    user = dict()
    user['nome'] = str(input('Nome: '))
    user['cpf'] = str(input('CPF: '))
    if '.' in user['cpf']:
        user['cpf'] = user['cpf'].replace('.', '')
        if '-' in user['cpf']:
            user['cpf'] = int(user['cpf'].replace('-', ''))
    user['cpf'] = int(user['cpf'])
    user['data_nascimento'] = str(input('Data de nascimento: '))
    logradouro = str(input('Logradouro: '))
    nro = str(input('Numero: '))
    bairro = str(input('Bairro: '))
    cidade = str(input('Cidade: '))
    sigla = str(input('UF: '))
    endereco = f'{logradouro.title()}, {nro} - {bairro.title()} - {cidade.title()}/{sigla.upper()}'
    user['endereço'] = endereco
    return user


def criar_conta(users):
    contas = []
    num_conta = 0
    cpf = int(input('Informe o cpf: '))
    if users:
        for i in users:
            for k, v in i.items():
                print(type(v))
                if v == cpf:
                    print(f'k, v = {k, v}')
                    print(f'v = {v}')
                    agencia = '0001'
                    num_conta += 10
                    usuario = users
                    new_conta = [agencia, num_conta, usuario]
                    contas.append(new_conta)
                    # print(len(contas))
    else:
        agencia = '0001'
        num_conta += 1
        new_usuer = new_user()
        new_conta = [agencia, num_conta, new_usuer]
        new_usuer = new_conta[2]
        contas.append(new_conta)
        users = new_usuer
        # print(len(contas))
        '''opcao = input('Digite -1- para novo usuario ou -2- para voltar ao menu anterior')
            if '2' in opcao:
                break'''
    return contas
    # , users


# encontrados = [p for p in pessoas if p['nome'] == nome or p['cpf'] == cpf]
'''
    while True:
        #cpf = input('Informe o cpf: ')
        if cpf in users:
            agencia = '0001'
            num_conta += 1
            usuario = users[cpf]
            new_conta = [agencia, num_conta, usuario]
            contas.append(new_conta)
        else:
            agencia = '0001'
            num_conta += 1
            usuario = new_user()
            new_conta = [agencia, num_conta, usuario]
            contas.append(new_conta)
            opcao = input('Digite -1- para novo usuario ou -2- para voltar ao menu anterior')
            if '2' in opcao:
                break
    return contas
'''

def menu():
    print('  MENU  '.center(30))
    print('*' * 30)
    print('1 - Depósito')
    print('2 - Saque')
    print('3 - Extrato')
    print('4 - Novo Cliente')
    print('5 - Abrir Conta')
    print('6 - Sair')
    print('*' * 30)
''' escolha = int(input('Digite sua opção: '))
    while True:
        if escolha == 1:
            valor = float(input('Digite o valor do deposito: '))
            if valor > 0:
                return deposito(saldo, valor)
            else:
                print('Valor invalido, deve ser maior que 0')
                escolha = int(input('Digite sua opção: '))
        elif escolha == 2:
            if num_saque > 0:
                valor = float(input('Digite o valor do saque: '))
                return saque(saldo=saldo, valor=valor, num_saques=num_saque, limite_saque=limite_saque)
            else:
                print('Voce ja fez os 3 saques do dia')
                escolha = int(input('Digite sua opção: '))
        elif escolha == 3:
            return extrato(saldo, movimentacoes)
        elif escolha == 4:
            return criar_conta(users=new_user())
        elif escolha == 5:
            return new_user()
        else:
            break
    return escolha
'''

# print(criar_conta())


# print(new_user())


# print(extrato(1000, extrato=[100, -456]))

#print(deposito(saldo, 345, movimentacoes=movimentacoes))


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
