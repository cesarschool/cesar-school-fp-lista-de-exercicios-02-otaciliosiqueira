## QUESTÃO 3 ##
# Implementar um programa que calcula o desconto previdenciário de um funcionário. 
# O programa deve, dado um salário, retornar o valor do desconto proporcional ao mesmo. 
# O cálculo de desconto segue a regra: o desconto deve 11% do valor do salário, entretanto, 
# o valor máximo de desconto é 318,20.
# Sendo assim, ou o programa retorna 11% sobre o salário ou 318,20.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    
    sal = float(input('Digite seu salário:  R$ '))
    desconto = 0.11 * sal

    if not desconto >= 318.20:
        print('De acordo com o seu salário(R$ {:.2f}) seu desconto(11%) é de R$ {:.2f}'.format(sal, desconto))
    else:
        desconto = 318.20 
        print('De acordo com o seu salário(R$ {:.2f}) seu desconto é de R$ {:.2f}'.format(sal, desconto))

        
if __name__ == '__main__':
    main()
