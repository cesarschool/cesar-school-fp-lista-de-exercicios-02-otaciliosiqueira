## QUESTÃO 6 ##
# Escreva um programa que calcule a porcentagem de nucleotídeos A, C, G e T em 
# uma cadeia de DNA informada pelo usuário. Indicar também a quantidade e a 
# porcentagem de nucleotídeos inválidos.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    seqDna = input('Digite uma sequência de DNA:  ').upper()
    porcentA = seqDna.count('A') / len(seqDna)*100
    porcentC = seqDna.count('C') / len(seqDna)*100
    porcentG = seqDna.count('G') / len(seqDna)*100
    porcentT = seqDna.count('T') / len(seqDna)*100

    porcentInvalidos = 100 - (porcentA + porcentC + porcentG + porcentT)
    print('Sequência de DNA informarda: {}\nPorcentagem de nucleotídeos A: {}\nPorcentagem de nucleotídeos C: {}\nPorcentagem de nucleotídeos G: {}\nPorcentagem de nucleotídeos T: {}\nPorcentagem de nucleotídeos Inválidos: {}\n' .format(seqDna, porcentA, porcentC, porcentG, porcentT, porcentInvalidos))


    
if __name__ == '__main__':
    main()
