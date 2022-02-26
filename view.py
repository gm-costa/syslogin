from os import system
from controller import *

traco = '-' * 44


def limpa_tela():
    system('clear') or None


def menu():
    limpa_tela()
    print(traco)
    print('MENU'.center(44, ' '))
    print(traco)
    print('[ 1 ] - Para cadastrar um usuário')
    print('[ 2 ] - Para alterar um usuário')
    print('[ 3 ] - Para remover um usuário')
    print('[ 4 ] - Para mostrar os usuários cadastrados')
    print('[ 5 ] - Para fazer login no sistema')
    print('[ 9 ] - Para Encerrar o sistema')
    print(traco)


def pausar(texto):
    print('\n' + texto)
    input('\nTecle <Enter> para continuar ')


if __name__ == '__main__':

    engine = ConfigController.cria_engine()
    sessao = ConfigController.cria_session(engine)
    ConfigController.cria_tabela(engine)

    while True:
        menu()
        try:
            opcao = int(input('Informe a opção: '))

            if opcao == 9:
                break

            if opcao == 1:
                limpa_tela()
                x = UsuarioController()
                print('\nInforme os dados do usuário para cadastro.')
                nome = input('\nNome: ').strip().upper()
                email = input('E-mail: ').strip().lower()
                senha = input('Senha: ').strip().upper()
                if len(nome) == 0:
                    pausar('Nome não informado!')
                elif (len(email) == 0):
                    pausar('E-mail não informado!')
                elif not '@' in email:
                    pausar('E-mail inválido!')
                elif len(senha) < 4:
                    pausar('A senha deve ter pelo menos 4 caracteres!')
                else:
                    if x.cadastrar_usuario(nome, email, senha, sessao) == 1:
                        pausar('Usuário cadastrado com sucesso.')
                    else:
                        pausar('Não foi possível cadastrar o usuário.')

            elif opcao == 2:
                limpa_tela()
                x = UsuarioController()
                id_usuario = int(input(
                    '\nInforme o código do usuário que deseja alterar: ').strip())
                if not x.existe_usuario(id_usuario, sessao):
                    pausar('Usuário não cadastrado!')
                else:
                    print('\nDeixar em branco os dados que NÃO deseja alterar')
                    nome = input('Nome: ').strip().upper()
                    email = input('E-mail: ').strip().lower()
                    senha = input('Senha: ').strip().upper()
                    if x.alterar_usuario(id_usuario, nome, email, senha, sessao) == 1:
                        pausar('Usuário alterado com sucesso.')
                    else:
                        pausar('Não foi possível alterar o usuário.')

            elif opcao == 3:
                limpa_tela()
                x = UsuarioController()
                id_usuario = int(input(
                    '\nInforme o código do usuário que deseja remover: ').strip())
                if not x.existe_usuario(id_usuario, sessao):
                    pausar('Usuário não cadastrado!')
                else:
                    if x.remover_usuario(id_usuario, sessao) == 1:
                        pausar('Usuário removido com sucesso.')
                    else:
                        pausar('Não foi possível alterar o usuário.')

            elif opcao == 4:
                limpa_tela()
                usuarios = UsuarioController.listar_usuarios(sessao)
                if len(usuarios) == 0:
                    pausar('Não existe usuário cadastrado!')
                else:
                    print('-' * 108)
                    print('Relação dos usuários cadastrados'.center(108, ' '))
                    print('-' * 108)
                    print(f" {'ID':3} {'NOME':50} {'E-MAIL'}")
                    print('-' * 108)
                    for u in usuarios:
                        print(f' {u.id:3} {u.nome:50} {u.email}')
                    print('-' * 108)
                input('\nTecle <Enter> para continuar ')

            elif opcao == 5:
                limpa_tela()
                pausar(str(opcao))
            # else:
            #     pausar('Opção inválida, tente novamente!')
        except:
            pausar(f'Opção inválida, tente novamente!')
