## QUESTÃO 1 ##
# Faça um programa que receba cinco inteiros e diga qual deles é o maior e qual o menor.
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    
    print('Digite cinco números inteiros e diferentes\n')

    n1 = int(input('Primeiro numero:  '))
    n2 = int(input('Segundo numero:  '))
    n3 = int(input('Terceiro numero:  '))
    n4 = int(input('Quarto numero:  '))
    n5 = int(input('Quinto numero:  '))	
    print('')

    if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
        print('{} é o maior número'.format(n1))

    elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
        print('{} é o maior número'.format(n2))

    elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
        print('{} é o maior número'.format(n3))

    elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
        print('{} é o maior número'.format(n4))

    elif n5 > n1 and n5 > n3 and n5 > n4 and n5 > n2:
        print('{} é o maior número'.format(n5))
    else:
        print('## ERRO ## - Você digitou números iguais')
   


if __name__ == '__main__':
    main()
