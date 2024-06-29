import os

restaurantes = [{'nome':'Cuscuz da Maria', 'categoria':'Nordestina', 'ativo':False}, 
               {'nome':'Sushi da Rina', 'categoria':'Japonesa', 'ativo':True}, 
               {'nome':'Abará da Dandara','categoria':'Baiana', 'ativo':True}]

def exibir_nome_do_programa():
    print("""
███╗░░░███╗░█████╗░██████╗░███╗░░░███╗██╗████████╗███████╗██████╗░░██████╗
████╗░████║██╔══██╗██╔══██╗████╗░████║██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝
██╔████╔██║███████║██████╔╝██╔████╔██║██║░░░██║░░░█████╗░░██████╔╝╚█████╗░
██║╚██╔╝██║██╔══██║██╔══██╗██║╚██╔╝██║██║░░░██║░░░██╔══╝░░██╔══██╗░╚═══██╗
██║░╚═╝░██║██║░░██║██║░░██║██║░╚═╝░██║██║░░░██║░░░███████╗██║░░██║██████╔╝
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░""")
    
def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante') 
    print('3. Aceitar Restaurante')
    print('4. Sair\n')     

def exibir_subtexto(texto):
    os.system('clear')
    linha = '█' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_ao_menu_principal():
    input('Digite uma tecla para retornar ao menu')
    main()

def cadastrar_novo_restaurante():
    exibir_subtexto('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: \n')
    categoria = input(f'Digite qual a categoria do restaurante {nome_do_restaurante} ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'\nO restaurante {nome_do_restaurante}, foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtexto('Restaurantes Disponíveis\n')
    print (f'{'Nome'.ljust(24)} {'Categoria'.ljust(24)} {'Status'}')
    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        status = 'Ativo' if restaurante['ativo'] else 'Inativo'
        print(f'- {nome.ljust(20)} | - {categoria.ljust(20)} | - {status.ljust(20)}')
    print()
    voltar_ao_menu_principal()

def modificar_status():
    exibir_subtexto('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True 
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso. ' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso. '
            print(mensagem)
         
        
    if not restaurante_encontrado: 
        print(f'O restaurante {nome_restaurante} não foi encontrado')

    voltar_ao_menu_principal()

def finalizar_app():
    exibir_subtexto('Finalizando o App\n')

def escolher_opcao():
    try:
        opção_escolhida = int(input('Escolha uma opção: '))
        
        if opção_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opção_escolhida == 2:
            listar_restaurantes()
        elif opção_escolhida == 3:
            modificar_status()
        elif opção_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()   
    except: 
        opcao_invalida()

def opcao_invalida():
    print('Opção Inválida')
    voltar_ao_menu_principal()

def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
