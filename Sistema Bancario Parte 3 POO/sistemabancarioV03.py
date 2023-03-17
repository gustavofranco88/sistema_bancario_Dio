import textwrap
from datetime import datetime
from abc import ABC, abstractmethod
# from time import sleep


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print('Operação falhou, saldo insuficiente')

        elif valor > 0:
            self._saldo -= valor
            print('saque realizado com sucesso')
            return True

        else:
            print('Operação falhou, valor invalido')
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('Deposito realizado com sucesso')

        else:
            print('Operação falhou, valor invalido')
            return False

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico._transacoes if transacao["tipo"] == Saque.__name__]
        ) + 1
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques > self.limite_saques

        if excedeu_limite:
            print('Valor excede o valor limite por saque')

        elif excedeu_saques:
            print('Voce ja fez os 3 saques do dia')

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agencia:\t{self.agencia}
            C/c:\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        add_transacao = {
            'tipo': transacao.__class__.__name__,
            'valor': transacao.valor,
            'data': datetime.now()  # .strftime('%d - %m -%y % H: % s'),
        }
        self._transacoes.append(add_transacao)


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def menu():
    print('*' * 30)
    print('BEM VINDO AO BANCO DIO'.center(30))
    print('*' * 30)
    print('  MENU  '.center(30))
    print('*' * 30)
    print('1 - Depósito')
    print('2 - Saque')
    print('3 - Extrato')
    print('4 - Novo Cliente')
    print('5 - Abrir Conta')
    print('6 - Exibir Contas')
    print('7 - Sair')
    print('*' * 30)
    opcao = input('Informe a opção desejada: ')
    return opcao


def filtrar_clientes(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recupera_conta_cliente(cliente):
    if not cliente.contas:
        print('Cliente não possui conta')
        return
    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]


def depositar(clientes):
    cpf = input('Informe o cpf do cliente: ')
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print('cliente não encontrado')
        return

    valor = float(input('Informe o valor do deposito: '))
    transacao = Deposito(valor)
    conta = recupera_conta_cliente(cliente)

    if not conta:
        return

    cliente = cliente
    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input('Digite o cpf do cliente: ')
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado!')
        return

    valor = float(input('Informe o valor do saque: '))
    transacao = Saque(valor)

    conta = recupera_conta_cliente(cliente)
    if not conta:
        return

    cliente = cliente
    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input('Digite o cpf do cliente: ')
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado!')
        return

    conta = recupera_conta_cliente(cliente)
    if not conta:
        return

    print('\n============== EXTRATO ===================')
    transacoes = conta.historico.transacoes

    extrato = ''
    if not transacoes:
        extrato = 'Não foram encontradas transaçoes.'

    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\t R${transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR${conta.saldo:.2f}")
    print('============================================')


def criar_cliente(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_clientes(cpf, clientes)

    if cliente:
        print('Já existe cliente cadastrado com este cpf!!!')
        return

    nome = input('Nome completo: ')
    data_nascimento = input('Data de nascimento (dd-mm-aaaa: ')
    endereco = input('Informe o endereco: Logradouro, nro - bairro - cidade/sigla do estado): ')

    cliente = PessoaFisica(cpf=cpf, nome=nome, data_nascimento=data_nascimento, endereco=endereco)

    clientes.append(cliente)

    print('Cliente cadastrado com sucesso!!!')


def criar_contas(numero_contas, clientes, contas):
    cpf = input('Infornme o CPF do cliente: ')
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado!')
        print('Fluxo de criação de conta, encerrado!!!')
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_contas)
    contas.append(conta)
    cliente.contas.append(conta)

    print('Conta criada com sucesso!!!')


def listar_contas(contas):
    for conta in contas:
        print('=' * 40)
        print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []

    while True:
        try:
            opcao = int(menu())
            if opcao == 1:
                depositar(clientes)

            elif opcao == 2:
                sacar(clientes)

            elif opcao == 3:
                exibir_extrato(clientes)

            elif opcao == 4:
                criar_cliente(clientes)

            elif opcao == 5:
                numero_conta = len(contas) + 1
                criar_contas(numero_conta, clientes, contas)

            elif opcao == 6:
                listar_contas(contas)

            elif opcao == 7:
                print('Saindo')
                break

            else:
                print('Olá, Digite uma opção valida')

        except ValueError:
            print('Digite uma opção valida')


main()