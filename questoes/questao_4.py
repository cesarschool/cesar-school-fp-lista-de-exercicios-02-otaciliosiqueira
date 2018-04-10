## QUESTÃO 4 ##
# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. 
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos 
# a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o 
# valor da prestação como sendo o valor da casa a comprar dividido pelo número de 
# meses a pagar.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    
    valCasa = float(input('Informe o valor da casa que pretende comprar: R$ '))
    sal = float(input('Informe o seu salário: R$ '))
    qtdAnos = int(input('Informe a quantidade de anos que pretende pagar: '))

    meses = qtdAnos*12
    prest = valCasa/meses

    if prest > 0.3*sal:
        print('Sua solicitação não foi aprovada. O valor excede ao valor para aprovação, seu salário(R${}) não é suficiente para as prestações calculadas.'.format(sal))
    else:
        print('Parabéns, sua solicitação foi aprovada. O valor da prestação ficará em {} X R${:.2f}'.format(meses, prest))


    
if __name__ == '__main__':
    main()
