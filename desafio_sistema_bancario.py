menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
taxa_saque = 0

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor de saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite 
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        taxa_saque = valor < saldo

        if excedeu_saldo:
            print("Erro! VocÊ não tem saldo suficiente.")

        elif excedeu_limite:
            print("Erro! Valor de saque excede o limite.")

        elif taxa_saque:
            saldo -= valor + 5
        
        elif excedeu_saques:
            print("Erro! Número máximo de saques excedido.")

        elif valor < 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Erro! O valor informado é inválido.")
    
    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

    