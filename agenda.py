AGENDA = {'Giovani': {"telefone": "11928198218",
        "email": "teste@giovani.com",
        "endereco": "avenida teste 1",},

        'Maria': {"telefone": "1198123723",
        "email": "teste@maria.com",
        "endereco": "avenida teste 2",},
}


def mostrar_contatos():
    try:
        for contato in AGENDA:
            buscar_contatos(contato)
            print('--------------------\n')
    except KeyError:
        print('Contato inexistente')
    except Exception as error:
        print('Algo de errado aconteceu')
        print(error)


def exportar_arquivo():
    try:
        with open('agenda.txt', 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write("Nome: {}\n,Telefone: {}\n,E-mail: {}\n,Endereco {}\n".format(contato,telefone,email,endereco + '\n'))
        print('Agenda exportada com sucesso')
    except:
        print('Algum erro aconteceu ao exportar os contatos')


def importar_contatos(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                print(linha.strip().split())
    except FileNotFoundError:
        print('Arquivo nao encontrado')
    except Exception as error:
        print('Erro inesperado')
        print(error)



def buscar_contatos(contato):
    try:
        print('Nome:', contato)
        print('telefone:', AGENDA[contato]['telefone'])
        print('email:', AGENDA[contato]['email'])
        print('endereco:', AGENDA[contato]['endereco'])
    except KeyError:
        print('Contato inexistente')
    except Exception as error:
        print('Algo de errado aconteceu')
        print(error)


def incluir_editar_contato(contato,telefone,email,endereco):
    try:
        AGENDA[contato] = \
            {"telefone": telefone,
             "email": email,
             "endereco": endereco,
             }
    except KeyError:
        print('Contato inexistente')
    except Exception as error:
        print('Algo de errado aconteceu')
        print(error)

    print('Contato {} adicionado ou editado com sucesso!'.format(contato))


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        print('Contato {} excluido com sucesso!'.format(contato))
    except KeyError:
        print('Contato inexistente')

    except Exception as error:
        print('Algo de errado aconteceu')
        print(error)


def imprimir_menu():
    print('Essas sao as opcoes da agenda')
    print('1- Mostrar todos os contatos')
    print('2- Editar um contato da agenda')
    print('3- Excluir um contato da agenda')
    print('4- Incluir um contato na agenda')
    print('5- Pesquisar um contato na agenda')
    print('6- Exportar agenda')
    print('7- Importar contatos')
    print('0- Fechar agenda\n')


def opcoes_agenda():
    imprimir_menu()
    try:
        OPCAO = input('O que deseja fazer na agenda?\n')
        if (OPCAO == '1'):
            mostrar_contatos()

        elif (OPCAO == '2'):
            mostrar_contatos()

            print('Qual contato quer editar?')
            nome_contato = input()
            buscar_contatos(nome_contato)
            print('\nQual nome deseja inserir no contato?')
            contato = input()

            print('Qual telefone gostaria de inserir?')
            telefone = input()

            print('Qual email deseja inserir?')
            email = input()

            print('Qual endereco deseja inserir?')
            endereco = input()

            incluir_editar_contato(contato, telefone, email, endereco)
            print('\nCaso deseje ver as alteracoes feitas no contato, aperte 1')
            ver_alteracoes = input()
            if (ver_alteracoes == '1'):
                print(buscar_contatos(contato))
            else:
                print('\nAs alteracoes ja foram salvas, obrigado por usar agenda!')

        elif (OPCAO == '3'):
            mostrar_contatos()
            print('Qual contato gostaria de excluir?')
            contato = input()
            excluir_contato(contato)

        elif (OPCAO == '4'):
            print('Insira o nome do seu novo contato')
            contato = input()
            print('Insira o telefone do seu novo contato')
            telefone = input()
            print('Insira o email do seu novo contato')
            email = input()
            print('Insira o endereco do seu novo contato')
            endereco = input()

            incluir_editar_contato(contato, telefone, email, endereco)

        elif (OPCAO == '5'):
            print('Qual o nome do contato que gostaria de pesquisar na agenda?')
            contato = input()
            print('\nSegue abaixo as informacoes do contato pesquisado:\n')
            buscar_contatos(contato)

        elif (OPCAO == '6'):
            exportar_arquivo()

        elif (OPCAO == '7'):
            nome_arquivo = input('Digite o nome do arquivo para ser importado\n')
            importar_contatos(nome_arquivo)

        elif (OPCAO == '0'):
            print('Agenda fechada. Te vejo na proxima consulta!')
        else:
            print('Escolha uma opcao valida!\n')
            opcoes_agenda()

    except Exception as error:
        print('Algo de errado aconteceu')
        print(error)



opcoes_agenda()