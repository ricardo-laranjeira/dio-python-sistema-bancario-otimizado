import textwrap

def menu():
    menu = """\n
    =====MENU=====
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tLista contas
    [nu]\tNovo usuario
    [q]\tSair
    ==> """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}"
        print("\nDeposito realizado com sucesso!")
    else:
        print("\nOperacao falhou! Valor informado invalido.")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_sques, limite_saques):
    if valor > saldo:
        print("Saldo insuficiente!")
    elif valor > limite:
        print("O valor do saque excede o limite!")
    elif numero_saques >= limite_saques:
        print("Numero de saques excedidos!")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}"
        numero_saques += 1
        print("Saque realizado com sucesso.")
    else:
        print("Valor informado invalido.")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n=====Extrato=====")
    print("Nao foram realizados movimentacoes" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n================")


def criar_usuario(usuarios):
    cpf = input("Informe o cpf (somente numeros): ")
    usuario = filtar_usuario(cpf, usuarios)

    if usuario:
        print("\nJa existe usuario com esse cpf!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nsacimento (dd-mm-aaa): ")
    endereco = input("Informe o endereco (logradouro, nr - bairro, cidade/uf): ")

    usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereco":endereco})

    print("Usuario criado com sucesso!")


def filtar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuario: ")
    usuario = filtar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso")
        return {"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}
    
    print("\n Usuario nao encontado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\n
            Agencia:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:
        opcao = menu()
        match opcao:
            case "d":
                valor = float(input("Informe o valor do deposito: "))
                saldo, extrato = depositar(saldo, valor, extrato)

            case "s": 
                valor = float(input("Informe o valor do saque: "))
                saldo, extrato = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_sques = LIMITE_SAQUES
                )
                
            case "e":
                exibir_extrato(saldo, extrato=extrato)
                
            case "nu":
                criar_usuario(usuarios)

            case "nc":
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)
                if conta:
                    contas.append(conta)


            case "lc":   
                listar_contas(contas)
            case "q":
                break
            case _:
                print("Opcao invalida.")

main()
