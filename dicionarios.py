import random
import pandas as pd
"""
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
"""
#Numero de telefone
"""numeros = {
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
"""

#Peca nome, data de nascimento, endereco e telefone para o usuario e guarde-os no dicionario
"""dados = {
    "nome": '',
    "nascimento": '',
    "endereco": '',
    "telefone": '',

}
pede_dados = {
    "nome" : 'Qual seu nome?',
    "nascimento": 'Qual seu nascimento?',
    "endereco": 'Qual seu endereco?',
    "telefone": 'Qual seu telefone?',

}

#Atribui a lista --> Q&A
for key in dados.keys():
    info = input(f"diga seu {key}")
    dados[key]= info

for key in dados.keys():
    dados[key] = [dados[key]]

print(dados)"""



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