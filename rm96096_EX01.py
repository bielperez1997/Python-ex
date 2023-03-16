""" Você foi procurado por um aluno do
curso de Produção Multimídia do FIAP ON
para desenvolver um trabalho em parceria: \
um serviço em que as pessoas possam usar
um estúdio profissional para gravar seus vídeos para
o YouTube com máxima qualidade. O serviço ganha
dinheiro por meio de um sistema de assinaturas e
de um bônus calculado por uma porcentagem sobre
o faturamento que o canal do cliente obteve ao longo
do ano.

Sua tarefa é criar um algoritmo que receba o
tipo de assinatura do cliente, o faturamento
anual dele e que calcule e exiba qual o valor
do bônus que o cliente deve pagar a vocês.A
tabela abaixo mostra a porcentagem de acordo
com cada nível de assinatura:

Nível

Porcentagem sobre o faturamento

Basic 30 %

Silver 20 %

Gold 10 %

Platinum 5 % """

valor_anual = float(input("Por favor, informe o seu faturamento anual: "))
assinatura = input("Por favor, informe o seu plano de assinatura: BASIC, SILVER, GOLD ou PLATINUM: ")
plano_assinatura_basic = "BASIC"
plano_assinatura_silver = "SILVER"
plano_assinatura_gold = "GOLD"
plano_assinatura_platinum = "PLATINUM"
valor_assinatura = 0
valor_liquido = int(valor_assinatura)
if assinatura.upper() == "BASIC":
    if plano_assinatura_basic == "BASIC":
        valor_assinatura = valor_anual * 0.3
        valor_liquido = int(valor_assinatura)
        print("O seu tipo de assinatura é {}. O seu faturamento anual foi de R${}. O valor do bônus a ser pago é de R${}.".format(plano_assinatura_basic, int(valor_anual), int(valor_liquido)))
elif assinatura.upper() == "SILVER":
    if plano_assinatura_silver == "SILVER":
        valor_assinatura = valor_anual * 0.2
        valor_liquido = int(valor_assinatura)
        print("O seu tipo de assinatura é {}. O seu faturamento anual foi de R${}. O valor do bônus a ser pago é de R${}.".format(plano_assinatura_silver, int(valor_anual), int(valor_liquido)))
elif assinatura.upper() == "GOLD":
    if plano_assinatura_gold == "GOLD":
        valor_assinatura = valor_anual * 0.1
        valor_liquido = int(valor_assinatura)
        print("O seu tipo de assinatura é {}. O seu faturamento anual foi de R${}. O valor do bônus a ser pago é de R${}.".format(plano_assinatura_gold, int(valor_anual), int(valor_liquido)))
elif assinatura.upper() == "PLATINUM":
    if plano_assinatura_platinum == "PLATINUM":
        valor_assinatura = valor_anual * 0.05
        valor_liquido = int(valor_assinatura)
        print("O seu tipo de assinatura é {}. O seu faturamento anual foi de R${}. O valor do bônus a ser pago é de R${}.".format(plano_assinatura_platinum, int(valor_anual), int(valor_liquido)))
else:
    print("Plano inexistente, por favor entrar em contato com o administrador do seu plano.")





