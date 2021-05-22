pessoas = {"Giovani": 20,
           "Dayane": 35,
           "Cristiano": 39
            }

#o objeto pessoas é uma chave, e caso seja printado o objeto, é exibido os dados do mesmo

#Caso seja usado em um for por exemplo, será exibido cada elemento do objeto

for pessoa in pessoas:
        print(pessoa)

#Se for usado a funcao .value no pessoas, será exibido os valores dentro de cada elemento no for

for pessoa in pessoas.values():
        print(pessoa)