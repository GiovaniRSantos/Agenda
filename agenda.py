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
        print('--------------------')


def buscar_contatos(contato):
    print('Nome:', contato)
    print('telefone:', AGENDA[contato]['telefone'])
    print('email:', AGENDA[contato]['email'])
    print('endereco:', AGENDA[contato]['endereco'])


def incluir_contato(contato,telefone,email,endereco):
    AGENDA[contato] = \
        {"telefone": telefone,
        "email": email,
        "endereco": endereco,
         }
    print('Contato {} adicionado com sucesso'.format(contato))

# buscar_contatos('Giovani')
incluir_contato('Paulo', '11928381723','teste@teste.com','avenida teste')
mostrar_contatos()