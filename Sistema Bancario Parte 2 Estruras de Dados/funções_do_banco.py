# criar funçoes de: +saque, +depósito, +extrato, +criar_user, +criar_conta
import textwrap


def saque(*, saldo, valor, num_saques, limite_saque, movimentacoes):
    """
    função para realizar saque da conta caso as regras sejam cumpridas. Precisa ser valor maior que zero,
        estar no limite de até 500 reais por saque e ter sacado menos de 3 vezes no mesmo dia
    :param saldo: saldo atual da conta, será decrementado o valor passado para o saque caso confirmado
    :param valor: valor a ser sacado
    :param num_saques: contagem de saques diarios
    :param limite_saque: valor máximo por saque
    :param movimentacoes: salva a transação para exibição no extrato
    :return: retorna o novo saldo caso seja efetuada a transação, ou o saque sem alteração
    """
    if valor > saldo or valor <= 0:
        print('Não é possivel sacar este valor')
        print(f'Saldo não alterado, Seu saldo atual é R${saldo:.2f}'.replace('.', ','))
    elif valor > limite_saque:
        print('escolha um valor de saque até 500')
        print(f'Saldo não alterado, Seu saldo atual é R${saldo:.2f}'.replace('.', ','))
    else:
        saldo -= valor
        movimentacoes.append(valor * (-1))
        num_saques -= 1
    return saldo, num_saques


def deposito(saldo, valor, movimentacoes, /):
    """
    função para depositar valor na conta
    :param saldo: valor atual para ser incrementado se operação for confirmada
    :param valor: valor que será depositado
    :param movimentacoes: salva a transação para exibir no extrato
    :return: novo valor em conta, caso operação seja realizada ou o mesmo valor se não for realizada
    """
    # dep = float(input('Digite o valor do depósito '))

    if valor > 0:
        saldo += valor
        movimentacoes.append(valor)
    else:
        print('Valor Invalido')
    return saldo


def extrato(saldo, /, *, movimentacoes):
    """
    função para exibir as transações e o saldo atual
    :param saldo: mostra o saldo atual da conta
    :param movimentacoes: salva as transações (deposito e saque), para exibir no extrato
    :return: retorna as movimentações ordenas pela ordem que foram executadas
    """
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


def criar_usuario(usuarios):
    """
    função para cadastrar novos usuarios
    :param usuarios: lista com usuarios já existentes
    :return: novo usuário caso ainda não exista
    """
    user = dict()
    cpf = input('Informe o cpf: ')
    if '.' in 'cpf':
        cpf = cpf.replace('.', '')
        if '-' in 'cpf':
            cpf = cpf.replace('-', '')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('Já exixte um cadastro com este cpf')
        return
    else:
        user['cpf'] = cpf
        user['nome'] = str(input('Nome: '))
        user['data_nascimento'] = str(input('Data de nascimento: '))
        logradouro = str(input('Logradouro: '))
        nro = str(input('Numero: '))
        bairro = str(input('Bairro: '))
        cidade = str(input('Cidade: '))
        sigla = str(input('UF: '))
        endereco = f'{logradouro.title()}, {nro} - {bairro.title()} - {cidade.title()}/{sigla.upper()}'
        user['endereço'] = endereco
        usuarios.append(user)

    print('Usuario criado com sucesso')


def filtrar_usuario(cpf, usuarios):
    """
    Filtar usuarios pelo cpf, para ver se ja existe
    :param cpf: usuario informa o cpf a ser filtrado
    :param usuarios: lista de usuarios para buscar o cpf
    :return: retorna o usuario caso o cpf seja encontrado
    """
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    """

    :param agencia: numero da agencia
    :param numero_conta: valor com o numero da conta a ser criada
    :param usuarios: lista de usuarios para vincular o cpf a conta criada
    :return: dicionario com usuario, agencia e numero da conta
    """
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Conta criada com sucesso')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

    print('Usuario não encontrado')


def lista_contas(contas):
    """

    :contas: parametro traz a lista com as contas criadas
    :return: string com dados das contas
    """
    for conta in contas:
        linha = f"""\
                    Agência:\t{conta['agencia']}
                    C/C:\t\t{conta['numero_conta']}
                    Titular:\t{conta['usuario']['nome']}
                """
        print("=" * 100)
        print(textwrap.dedent(linha))
    return 'nenhuma conta criada'


def menu():
    """
    Mostra as opções de escolha do usuário
    """
    print('  MENU  '.center(30))
    print('*' * 30)
    print('1 - Depósito')
    print('2 - Saque')
    print('3 - Extrato')
    print('4 - Novo Cliente')
    print('5 - Abrir Conta')
    print(' - Exibir Contas')
    print('7 - Sair')
    print('*' * 30)
