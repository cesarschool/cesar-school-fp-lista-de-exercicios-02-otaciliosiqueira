## QUESTÃO 5 ##
# Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é 
# Equilátero, Isósceles ou Escaleno.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    
    a = float(input('Digite o valor do primeiro lado:  '))
    b = float(input('Digite o valor do segundo lado:  '))
    c = float(input('Digite o valor do terceiro lado:  '))

    print('\nDe acordo com os valores digitados temos um triângulo:\n')
    if a == b and b == c:
        print('EQUILATERO')
    elif a == b or a == c or b == c:
        print('ISOSCELES')
    else:
        print('ESCALENO')
        
if __name__ == '__main__':
    main()
