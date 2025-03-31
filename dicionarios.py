"""import random
import pandas as pd

dic = {'chave' : 'valor'}

#Printa dicionario (chave e valor)
print(dic)
print(dic.keys())
print(dic['chave'])

#cant access key through value
print(dic['valor']) # --> doesnt work

#Criar nova chave:
dic['nova chave'] = 'novo valor'
print(dic)

#Mudar valor da chave:
dic['chave'] = 'outro valor'
print(dic)

#Explorando indice
saudacoes = {
    'oi' : ['ola', 'e ai', 'salve'],
    'tchau' : ['flw', 'e nois', 'adeus']
}
#Indice
print(saudacoes['oi'][1]) # --> printa "e ai

resposta = input("Diga oi ou tchau")
#1st way to print
print(random.choice(saudacoes[resposta]))

#2nd way to print
aleatorio = random.randint(0, len(saudacoes[resposta])-1)
print(saudacoes[resposta][aleatorio])

#Numero de telefone
numeros = {
    'um' : '1',
    'dois' : '2',
    'tres' : '3',
    'quatro' : '4',
    'cinco' : '5',
    'seis' : '6',
    'sete' : '7',
    'oito' : '8',
    'nove' : '9'
}

numero = ''
for i in range(9):
    num = input(f"Diga seu {i+1} numero do seu telefone")
    numero += numeros[num]
print(f"Seu melhore numero:{numero}" )


#Peca nome, data de nascimento, endereco e telefone para o usuario e guarde-os no dicionario
dados = {
    "nome": '',
    "nascimento": '',
    "endereco": '',
    "telefone": '',

}


#Atribui a lista --> Q&A
for key in dados.keys():
    info = input(f"diga seu {key}")
    dados[key]= info

for key in dados.keys():
    dados[key] = [dados[key]]

print(dados)



#Cria dicionario com chave par e impar, cada chave coloca na lista com cada num par e impar repectivamente
par_impar = {
    'par' : [],
    'impar' : []
}

for i in range(20):
    if i%2 == 0:
        par_impar['par'].append(i)
    else:
        par_impar['impar'].append(i)
print(pd.DataFrame(par_impar))


#Itens em comum e adicionar a terceira lista
dic_1 = {
    "nome" : 'Pietro',
    "nascimento": '2006',
    "endereco": 'atibaia',
    "telefone": '190857376',
}
dic_2 = {
    "nome" : 'Pietro',
    "nascimento": '2006',
    "endereco": 'atibaia',
    "telefone": '11994731578',
}
dic_3 = {}

#Junta no valor da chave
for keys in dic_1.keys():
    for key in dic_2.keys():
        if dic_1[keys] == dic_2[key]:
            dic_3[keys] = dic_2[key]
print(dic_3)

#Lista em comum, justar no mesmo dicionario
dic_1 = {
    "nome" : ['Pietro','Joao'],
    "nascimento": ['2006',"2004"],
    "endereco": ['atibaia','SP'],
    "telefone": ['908357376', '1199467536'],
}
dic_2 = {
    "nome" : ['Arthur', 'Pedro'],
    "nascimento": ['2007','2016'],
    "endereco": ['Ourinhos', 'Itatiba'],
    "telefone": ['11994731578','5151435664'],
}
dic_3 = {

}

for key_1 in dic_1.keys():
    if key_1 in dic_2.keys():
        dic_3[key_1] = dic_1[key_1] + dic_2[key_1]
print(dic_3)


#Adiciona chaves unicas de cada lista para a terceira lista
dic_1 = {
    "nome" : ['Pietro','Joao'],
    "endereco": ['atibaia','SP'],
    "telefone": ['908357376', '1199467536'],
}
dic_2 = {
    "nome" : ['Arthur', 'Pedro'],
    "nascimento": ['2007','2016'],
    "telefone": ['11994731578','5151435664'],
}
dic_3 = {

}
for keys in dic_1.keys():
    if keys not in dic_2.keys():
        dic_3[keys] = dic_1[keys]
for key in dic_2.keys():
    if key not in dic_1.keys():
        dic_3[key] = dic_2[key]

print(dic_3)

#Encontra info carros

def forca_opcao(opcoes, msg):
    possibilidades = '\n'.join(opcoes)
    opcao = input(f"{msg}\n{possibilidades}\n->")
    while opcao not in opcoes:
        print("opcao invalida")
        opcao = input(f"{msg}\n{possibilidades}\n->")

    return opcao
def acha_indice(lista, elem):
    for i in range(len(lista)):
        if elem == lista[i]:
            return i
    return False

dic = {
    'modelo' : ['uno', 'kombi', 'fox'],
    'potencia' : ['450', '30', '50'],
    'preco' : ['100', '30', '50'],
    'ano' : ['2003', '1977', '2014'],
}

indices = {dic["modelo"][i] : i for i in range(len(dic["modelo"]))}

carro = forca_opcao(dic["modelo"],"qual carro voce quer?")
#indice = acha_indice(dic['modelo'], carro)
indice = indices[carro]
for key in dic.keys():
    print(f"{key} : {dic[key][indice]}")
"""

#in memory db / list comprehension

emojis = {
    ":)" : "😄",
    ";)" : "😉",
    ":o" : "😮"
}


def get_emoji(frase):
    for key in emojis.keys():
        frase = frase.replace(key, emojis[key])
    print(f"{frase}")
    return



frase = input("Escreva seu emoji favorito: ")
get_emoji(frase)