import matplotlib.pyplot as plt


def cria_matriz(lines, columns):
    matriz = []
    for i in range(lines):
        line = []
        for j in range(columns):
            line.append(0)
        matriz.append(line)
    return matriz


def mostra_matriz(matriz):
    for i in matriz:
        print(i)


def diagonal(matriz):
    for i in range(len(matriz)):
        matriz[i][i] = 1
    return matriz


def diagonal_contraria(matriz):
    for i in range(len(matriz)):
        matriz[i][len(matriz)-1-i] = 1
    return matriz

def abaixo(matriz):
    for i in range(len(matriz)):
        for j in range(i):
            matriz[i][j]=1
    return matriz

def acima(matriz):
    for i in range(len(matriz)):
        for j in range(i):
            matriz[j][i]=1
    return matriz

def transposta(matriz):
    for i in range(len(matriz)):
        for j in range(i+1, len(matriz)):
            aux = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = aux

    return matriz

def chess (matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if (i+j)%2 == 0:
                matriz[i][j] = 1
    return matriz



def medias_ponderadas(notas, pesos):
    medias = []
    for aluno in notas:
        soma_ponderada = 0
        for i in range(len(aluno)):
            soma_ponderada += aluno[i] * pesos[i]
        soma_pesos = sum(pesos)
        media = soma_ponderada / soma_pesos
        medias.append(media)
    return medias

notas = [[6, 4, 2, 0, 3, 7, 2, 10, 5, 1], [1, 5, 5, 6, 7, 8, 2, 8, 8, 4], [9, 4, 10, 10, 5, 9, 1, 2, 9, 0], [10, 5, 7, 4, 6, 6, 7, 4, 7, 1], [4, 4, 3, 0, 3, 3, 0, 0, 10, 0]]
pesos = [1,2,3,2,1]
medias = medias_ponderadas(notas, pesos)





def soma_lista(lista):
    soma = 0
    for elem in lista:
        soma += elem
    return soma


notas = [[6, 4, 2, 0, 3, 7, 2, 10, 5, 1], [1, 5, 5, 6, 7, 8, 2, 8, 8, 4], [9, 4, 10, 10, 5, 9, 1, 2, 9, 0], [10, 5, 7, 4, 6, 6, 7, 4, 7, 1], [4, 4, 3, 0, 3, 3, 0, 0, 10, 0]]
mostra_matriz(notas)
pesos = [1,2,3,2,1]
soma_pesos = soma_lista(pesos)
notas_finais = []



for j in range(len(notas[0])):
    soma = 0
    for i in range(len(pesos)):
        soma += pesos[i]*notas[i][j]
    soma/= soma_pesos
    notas_finais.append(round(soma,2))
print(notas_finais)








"""plt.imshow(matriz)
plt.colorbar()
plt.show()"""