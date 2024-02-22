cinema = []
informações = []
lugar = []

def cadeiras_cinema():
    print('''  
        __1 2 3 4 5 6 7 8 9 1²2²3³
        A · · · · · · · · · · · ·
        B · · · · · · · · · · · ·
        C · · · · · · · · · · · ·
        D · · · · · · · · · · · ·
        E · · · · · · · · · · · ·
        F · · · · · · · · · · · ·
        G · · · · · · · · · · · ·  
          ''')

def reserva():
    print(cadeiras_cinema)
    nome = input('Insira seu nome: ')
    informações.append(nome)
    fileira = input('Fileira:')
    informações.append(fileira)
    coluna = int(input('Coluna:'))
    informações.append(coluna)
    sexo = input('Sexo:')
   
    if sexo not in 'M, m, F, f':
        print('Preencha novamente')
        sexo = input('Sexo:')
    elif sexo in 'M, m, F, f':
        print()
    else:
        return
       
    informações.append(sexo)
    idade = int(input('Qual sua idade?'))
    informações.append(idade)
    
   
    if idade <= 12:
        print('O preço fica de R$ 12,00 reais')
        informações.append(12)
        
    elif idade >= 13:
        print('O preço fica de R$ 24,00 reais')
        informações.append(24)
       
    elif idade <= 60:
        print('Será feito de graça')
        informações.append(0)
        
    else:
        return(menu1)
    
    cinema.append(informações)
    
    
    with open('cinema.txt', 'a') as f:
        for items in cinema: 
            f.write('%s\n' %items) 
    print("Reserva feita com sucesso!") 
    f.close()

    print('''  
          1 - Voltar para o menu
          2 - Fazer Nova reserva
          ''')
    escolha2 = int(input('escolha dentre as alternativas anteriopres:'))
   
    if escolha2 == 1:
        menu()
    elif escolha2 == 2:
        reserva()
    else:
        print()

    print()
     
def dados_da_reserva():
    
    letra = input('fileira: ')
    numero = int(input('Insira o nuemro da cadeira: '))
    
    with open('cinema.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        linhas = conteudo.split('\n')
        for linha in linhas:
            if letra in linha:
                with open('cinema.txt', 'r') as arquivo:
                    for linha in arquivo:
                        palavras = linha.split()
                        if len(palavras) >= 3: 
                            parte1 = palavras[0]
                            parte2 = palavras[1]
                            parte3 = palavras[2]
                            parte4 = palavras[3]
                            parte5 = palavras[4]
                            parte6 = palavras[5]
                            print(f'''
                                A reserva está no nome de:{parte1}.
                                A sua fileira é:{parte2}, sua poltrona seria:{parte3}.
                                Seu sexo é:{parte4}.
                                Sua idade é de:{parte5} anos.
                                Você irá pagar:R${parte6} reais.
                                ''')
    arquivo.close()
    
    print()
   

def menu():
    print("""
        1 - Reserva
        2 - Dados da reserva
        3 - Fazer reservas de multiplos assentos
        4 - Anular reserva
        5 - Vizualizar reserva
        """)
    escolha = int(input('Escolha alguma das alternativas anteriores: '))


    if escolha == 1:
        reserva()
    elif escolha == 2:
        dados_da_reserva()
    elif escolha == 3:
        fazer_reservas_m()
    elif escolha == 4:
        anular_reserva()
    elif escolha == 5:
        vizualizar_reserva()
    else:
        escolha

def fazer_reservas_m():
    print(cadeiras_cinema)
    nome = input('Insira seu nome: ')
    informações.append(nome)
    linha2 = input('Fileira:')
    informações.append(linha2)
    inicio_linha = int(input('Primeiro assento:'))
    limite_linha = int(input('Ultimo assento:'))
    
    for L in range(inicio_linha, limite_linha):
        lugar.append(L)
    
    informações.append(lugar)
    sexo2 = input('Seu sexo:')
    informações.append(sexo2)
    idade2 = int(input('idade:'))
    informações.append(idade2)

    cinema.append(informações)

    if sexo2 not in 'M, m, F, f':
        print('Preencha novamente')
        sexo2 = input('Sexo:')
    elif sexo2 in 'M, m, F, f':
        print()
    else:
        return
   
    if idade2 <= 12:
        print('O preço fica de R$ 12,00 reais para cada pessoa')
        valor12 = L * 12
        print(f'o valos ao todo fica de {valor12} reais')
        informações.append(valor12)
    elif idade2 >= 13:
        print('O preço fica de R$ 24,00 reais para cada pessoa')
        valor24 = L * 24
        print(f'o valos ao todo fica de {valor24} reais')
        informações.append(valor24)
    elif idade2 <= 60:
        print('Será feito de graça para cada pessoa')
        informações.append(0)
    else:
        return(menu1)
    
    with open('cinema.txt', 'a') as f:
        for items in cinema: 
            f.write('%s\n' %items) 
    print("Reserva feita com sucesso!") 
    f.close()
 
    print('''  
          1 - Voltar para o menu
          2 - Fazer Nova reserva
          ''')
    escolha2 = int(input('escolha dentre as alternativas anteriopres:'))
   
    if escolha2 == 1:
        menu()
    elif escolha2 == 2:
        dados_da_reserva()
    else:
        print()
   
    print()

def anular_reserva():
    with open('cinema.txt', 'r+') as f:
        linhas = f.readlines()
        
        numero_linha_a_excluir = int(input('Insira o numero da tua reserva:'))

        if 1 <= numero_linha_a_excluir <= len(linhas):
            f.seek(0)
            
            linhas.pop(numero_linha_a_excluir - 1)
            
            f.writelines(linhas)

            f.truncate()
            
            print(f'Linha {numero_linha_a_excluir} removida com sucesso.')
        else:
            print(f'Linha {numero_linha_a_excluir} não encontrada.')
            
    print('Vamos te redirecionar para o menu novamente!')
    menu()


def vizualizar_reserva():
    print()

menu1 = menu()