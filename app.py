import os

restaurantes = [{'nome':'Praça','categoria':'japonesa','ativo':False},
                {'nome':'pizza','categoria':'italiana','ativo':True},
                {'nome':'self','categoria':'brasileira','ativo':False}]

def exibir_nome_do_programa():
    print('''
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
''')

def exibir_opções():
    print('1 - cadastrar restaurante')
    print('2 - Listar restaurante')
    print('3 - Alternar estado do restaurante')
    print('4 - Sair restaurante\n')

def finalizar_app():
    exibir_subtitulo('Finalizar App\n')

def exibir_subtitulo(texto):
    os.system('clear')
    linha = '*' * (len(texto))
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    print('Opção invalida')
    voltar_menu_principal()

def cadastar_novo_restaurante():
    '''Essa funcão para cadastro de restaurantes'''
    exibir_subtitulo('Cadastar restaurante\n')
    
    nome_do_restaurante = input('digite o nome do restaurante:  ')
    
    categoria = input(f'Digite o tipo de categoria do restaurante {nome_do_restaurante}:  ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria,'ativo':False }
    
    restaurantes.append(dados_do_restaurante)
    
    print(f'\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso.')

    voltar_menu_principal()



def listar_restaurantes():
    
    exibir_subtitulo('Listar restaurantes\n')
    
    print(f'{'NOME DO RESTAURANTE'.ljust(21)} | {'CATEGORIA'.ljust(20)} | STATUS ')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativo' if restaurante['ativo'] else 'desativado'
        print(f'.{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo} ')
      
    
    voltar_menu_principal()


def alternar_estado_restaurante():
    exibir_subtitulo('Alternar estado do restaurante:')   

    nome_restaurante = input('Digite o nome do restaurante:')

    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'o restaurante{nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O resataurante não foi encontrado')        
    
    voltar_menu_principal()


def voltar_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastar_novo_restaurante()        
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()

    except:
        opcao_invalida()
        



def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opções()
    escolher_opcao()
    


if __name__ == '__main__':
    main()