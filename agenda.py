AGENDA = {'Giovani': {"telefone": "11928198218",
        "email": "teste@giovani.com",
        "endereco": "avenida teste 1",},

        'Maria': {"telefone": "1198123723",
        "email": "teste@maria.com",
        "endereco": "avenida teste 2",},
}


def mostrar_contatos():
    for contato in AGENDA:
        buscar_contatos(contato)
        print('--------------------\n')


def buscar_contatos(contato):
    print('Nome:', contato)
    print('telefone:', AGENDA[contato]['telefone'])
    print('email:', AGENDA[contato]['email'])
    print('endereco:', AGENDA[contato]['endereco'])


def incluir_editar_contato(contato,telefone,email,endereco):
    AGENDA[contato] = \
        {"telefone": telefone,
        "email": email,
        "endereco": endereco,
         }
    print('Contato {} adicionado ou editado com sucesso!'.format(contato))


def excluir_contato(contato):
    AGENDA.pop(contato)
    print('Contato {} excluido com sucesso!'.format(contato))


def imprimir_menu():
    print('Essas sao as opcoes da agenda\n')
    print('1- Mostrar todos os contatos\n')
    print('2- Editar um contato da agenda\n')
    print('3- Excluir um contato da agenda\n')
    print('4- Incluir um contato na agenda\n')
    print('5- Pesquisar um contato na agenda\n')
    print('0- Fechar agenda\n')


def opcoes_agenda():
    imprimir_menu()
    OPCAO = input('O que deseja fazer na agenda?\n')
    if (OPCAO == '1'):
        mostrar_contatos()

    if (OPCAO == '2'):
        mostrar_contatos()

        print('Qual nome editar inserir?')
        nome_contato = input()
        buscar_contatos(nome_contato)
        print('\nQual nome deseja inserir no lugar?')
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
        if(ver_alteracoes == '1'):
            print(buscar_contatos(contato))
        else:
            print('\nAs alteracoes ja foram salvas, obrigado por usar agenda!')

    if (OPCAO == '3'):
        mostrar_contatos()
        print('Qual contato gostaria de excluir?')
        contato = input()
        excluir_contato(contato)

    if (OPCAO == '4'):
        print('Insira o nome do seu novo contato')
        contato = input()
        print('Insira o telefone do seu novo contato')
        telefone = input()
        print('Insira o email do seu novo contato')
        email = input()
        print('Insira o endereco do seu novo contato')
        endereco = input()

        incluir_editar_contato(contato, telefone, email, endereco)

    if (OPCAO == '5'):
        print('Qual o nome do contato que gostaria de pesquisar na agenda?')
        contato = input()
        print('\nSegue abaixo as informacoes do contato pesquisado:\n')
        buscar_contatos(contato)

    if (OPCAO == '0'):
        print('Agenda fechada. Te vejo na proxima consulta!')


opcoes_agenda()