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



def get_info(lista, index):
    for key in lista.keys():
        print(f"{key} : {lista[key][index]}")
    return
"""
carro = input("Qual carro voce gostaria de ver" + "\n" + "-->")


indice = acha_indice(carros["nomes"], carro)

get_info(carros, indice)

"""

#3 – Use o dicionário do item anterior para trazer todas as informações
#sobre o carro mais caro

def carro_mais_caro(lista):
    index = lista['preço'].index(max(lista['preço']))
"""
indice_caro = carro_mais_caro(carros)
get_info(carros, indice_caro)"""

#4 – Use o dicionário do item anterior para trazer todas as informações
#sobre o carro mais barato

def carro_mais_barato(lista):
    index = lista['preço'].index(min(lista['preço']))
    return index
"""
indice_barato = carro_mais_barato(carros)
get_info(carros, indice_barato)"""

#5 – Pergunte ao usuário se ele gostaria de cadastrar um novo carro e
#implemente esta funcionalidade

def cria_carro(lista):
    for key in lista.keys():
        resposta = input(f"Diga o novo {key}")
        lista[key].append(resposta)
    print(carros)
"""
cria_carro(carros)
"""
#6 – Pergunte ao usuário se ele gostaria de remover um carro e
#implemente esta funcionalidade


carros = {
    'nomes' : ['celta','up','kombi','uno'],
    'portas' : [4,2,6,2],
    'preço' : [1000,200,300,100],
    'ano de fabricação' : [2014,2018,1970,2005]
}


def acha_indice(lista, elem):
    for i in range(len(lista)):
        if elem == lista[i]:
            return i
    return

def remove(lista):
    resposta = input("Qual info de carro quer remover?")
    i = acha_indice(lista['nomes'], resposta)
    for key in lista.keys():
        lista[key].pop(i)
    print(lista)
    return



#7- Escreva um código capaz de contar a quantidade de vezes que uma
#palavra aparece numa frase, por exemplo:

frase = ("O bispo de Constantinopla é um bom desconstantinopolitanizador. Quem o "
         "desconstantinopolitanizar, um bom desconstantinopolitanizador será")
for char in ",.!?;:()":
    frase = frase.replace(char," ")
frase = frase.lower()
frase = frase.split(" ")
palavras = {}

for palavra in frase:
    if palavra not in palavras.keys():
        palavras[palavra] = 1
    else:
        palavras[palavra] +=1
print(palavras)