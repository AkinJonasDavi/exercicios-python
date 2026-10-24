valor_total = float(input("Digite o valor total da compra: R$ "))


print("\nESCOLHA A SUA FORMA DE PAGAMENTO:")
print("[1] À vista no PIX (10% de desconto)")
print("[2] Cartão de Crédito")

forma_pagamento = int(input("Escolha a opção (1 ou 2): "))

if forma_pagamento == 1:
    desconto = valor_total * 0.10
    valor_final = valor_total - desconto
    print(f"\n Pagamento no PIX aprovado!")
    print(f" Desconto concedido: R$ {desconto:.2f}")
    print(f" Valor final a pagar: R$ {valor_final:.2f}")

elif forma_pagamento == 2:
    parcelas = int(input("Digite a quantia de parcelas: "))
    
    if parcelas > 0 and parcelas <= 2:
        valor_parcela = valor_total / parcelas
        print(f"\n Pagamento em {parcelas}x sem juros.")
        print(f" Valor de cada parcela: R$ {valor_parcela:.2f}")
        print(f" Total da compra: R$ {valor_total:.2f}")
        
    elif parcelas >= 3:
        juros = valor_total * 0.05
        valor_final = valor_total + juros
        valor_parcela = valor_final / parcelas
        print(f"\n Pagamento em {parcelas}x com 5% de juros.")
        print(f" Valor do acréscimo: R$ {juros:.2f}")
        print(f" Valor de cada parcela: R$ {valor_parcela:.2f}")
        print(f" Total da compra: R$ {valor_final:.2f}")
        
    else:
        print("\n[ERRO] Número de parcelas inválido!")

else:
    print("\n[ERRO] Opção de pagamento inválida! Tente novamente.")