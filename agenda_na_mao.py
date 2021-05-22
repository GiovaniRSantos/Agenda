AGENDA = {
    "Giovani": {
        "telefone": "11928198218",
        "email": "teste@giovani.com",
        "endereco": "avenida teste 1"
    },
    "Maria":{
        "telefone": "1192811238",
        "email": "teste@maria.com",
        "endereco": "avenida teste 2"
    },
    "Joao":{
        "telefone": "11981937888",
        "email": "teste@joao.com",
        "endereco": "avenida teste 3"
    }
}

#Alterar dados

AGENDA['Giovani']['endereco'] = 'Rua nova alterada'
AGENDA['Giovani']['telefone'] = '1197070707070'

for contato in AGENDA:
    print(contato)