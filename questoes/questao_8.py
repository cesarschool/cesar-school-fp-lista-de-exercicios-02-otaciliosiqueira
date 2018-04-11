## QUESTÃO 8 ##
# Escreva um programa que leia uma data do usuário e calcule seu sucessor imediato.
# Por exemplo, se o usuário inserir valores que representem 2013-11-18, seu programa 
# deve exibir uma mensagem indicando que o dia imediatamente após 2013-11-18 é 
# 2013-11-19. Se o usuário inserir valores que representem 2013-11-30, o programa deve 
# indicar que o dia seguinte é 2013-12-01. Se o usuário inserir valores que representem 
# 2013-12-31 então o programa deve indicar que o dia seguinte é 2014-01-01. A data 
# será inserida em formato numérico com três instruções de entrada separadas; 
# uma para o ano, uma para o mês e uma para o dia. Certifique-se de que o seu programa 
# funciona corretamente para anos bissextos.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    
    ano = int(input('Digite o ano: '))
    mes = int(input('Digite o mês: '))
    dia = int(input('Digite o dia: '))


    anoBissexto = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
    cond = False


    if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
        if dia==31:
            if mes==12:
                mes = 1
                ano = ano + 1
            else:
                mes = mes + 1
            dia = 1
        elif (dia>31 or dia<=0):
            print('ENTRADA INVALIDA DIA')
        elif (mes>12 or mes<=0):
            print('ENTRADA INVALIDA MES')
        else:
            dia = dia + 1
    elif (mes==4 or mes==6 or mes==9 or mes==11):
        if dia==30:
            mes = mes + 1
            dia = 1
        elif (dia>30 or dia<=0):
            print('ENTRADA INVALIDA')
        elif (mes>12 or mes<=0):
            print('ENTRADA INVALIDA MES')
        else:
            dia = dia + 1

    elif mes==2:

        if anoBissexto:
            if dia<=0 or dia>29:
                print('ENTRADA INCORRETA')
            else:
                if dia==29:
                    dia = 1
                    mes = mes + 1
                else:
                    dia = dia + 1


        ## Se não for bissexto
        else:
            if dia<=0 or dia>28:
                print('ENTRADA INCORRETA')
            else:
                if dia==28:
                    dia = 1
                    mes = mes + 1
                else:
                    dia = dia + 1
    else:
        print('ENTRADA INCORRETA')

    print('Dia posterior: {}-{}-{}'.format(ano, mes, dia))


    
if __name__ == '__main__':
    main()
