AGENDA = {}

AGENDA['Giovani'] = {"telefone": "11928198218",
        "email": "teste@giovani.com",
        "endereco": "avenida teste 1",}


def mostrar_contatos():
    for contato in AGENDA:
        print('Nome:', contato)
        print('telefone:',AGENDA[contato]['telefone'])
        print('email:',AGENDA[contato]['email'])
        print('endereco:',AGENDA[contato]['endereco'])


mostrar_contatos()