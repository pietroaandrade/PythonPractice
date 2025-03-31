#1 – Modifique o seguinte Código para eliminar o uso de condicionais

import random
#Resp = input(“Diga oi ou tchau”)
#If resp == ‘oi’:
#Print(“olá”)
#Else:
#Print(“falou”)
"""
saudacoes = {
    "oi" : ["ola", "Bom dia"],
    "tchau" : ["falou", "ate mais"]
}
frase = input("de oi ou tchau")

print(random.choice(saudacoes[frase]))"""

#2 – Traga ao usuário todas as informações sobre um carro de sua
#escolha:

carros = {
    'nomes' : ['celta','up','kombi','uno'],
    'portas' : [4,2,6,2],
    'preço' : [1000,200,300,100],
    'ano de fabricação' : [2014,2018,1970,2005]
}

"""
def acha_indice(lista, elem):
    for i in range(len(lista)):
        if elem == lista[i]:
            return i
    return
def get_info(lista, index):
    for key in lista.keys():
        print(f"{key} : {lista[key][index]}")
    return

carro = input("Qual carro voce gostaria de ver" + "\n" + "-->")


indice = acha_indice(carros["nomes"], carro)

get_info(carros, indice)

"""

#3 – Use o dicionário do item anterior para trazer todas as informações
#sobre o carro mais caro


def acha_caro(lista):
    for key in lista.keys():

def acha_indice(lista, elem):
    for i in range(len(lista)):
        if elem == lista[i]:
            return i