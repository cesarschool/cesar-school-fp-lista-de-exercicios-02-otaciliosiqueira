## QUESTÃO 2 ##
# Uma forma de avaliar se uma pessoa está acima do peso é através do calculo do índice IMC. 
# Se o valor do IMC estiver acima de 25, significa que a pessoa está acima do peso. 
# A fórmula é: IMC = Peso(Kg) / (Altura(m)*Altura(m)). Com base na altura e peso fornecido no 
# console exiba uma mensagem determinando se uma pessoa está acima do peso.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    peso = float(input('Digite seu peso (Kg): '))
    altura = float(input('Digite sua altura (m): '))
    imc = peso / (altura ** 2)

    if not imc > 25:
        print('Você está na faixa de peso ideal. Seu IMC é {:.2f}'.format(imc))
    else:
        print('Você está acima do peso ideal. Seu IMC é {:.2f}'.format(imc))
    

if __name__ == '__main__':
    main()
