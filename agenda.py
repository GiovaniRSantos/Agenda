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


buscar_contatos('Giovani')