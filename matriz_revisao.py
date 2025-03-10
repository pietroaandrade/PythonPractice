import matplotlib.pyplot as plt



"""matriz = [[1,2,7],[3,4,8],[5,6,9]]"""
"""print(matriz[0])"""
"""for i in range(len(matriz)):
    for j in range(len(matriz)):
        print(matriz[i][j])"""
def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)
    return
def cria_matriz(linhas,colunas):
    matriz=[]
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz



"""for i in range(len(matriz_diagonal)):
    for j in range(len(matriz_diagonal)):
        if i == j:
            matriz_diagonal[i][j] = 1
            """
"""for i in range(len(matriz_diagonal)):
    matriz_diagonal[i][i] = 1
"""

def matriz_contraria(matriz):
    for i in range(len(matriz)):
        matriz[i][len(matriz)-1-i] = 1
    return matriz




def abaixo_diagonal(matriz):
    for i in range(len(matriz)):
        for j in range(i):
            matriz[i][j] = 1
    return matriz

def acima_diagonal(matriz):
    for i in range(len(matriz)):
        for j in range(i+1, len(matriz)):
            matriz[i][j] = 1
    return matriz

def transposta(matriz):
    for i in range(len(matriz)):
        for j in range(i+1, len(matriz)):
            aux = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = aux

    return matriz




def chess(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if (i+j) % 2 == 0:
                matriz[i][j] = 1
            else:
                matriz[i][j] = 0
    return matriz


#Exercício 7
notas = [[6, 4, 2, 0, 3, 7, 2, 10, 5, 1], [1, 5, 5, 6, 7, 8, 2, 8, 8, 4], [9, 4, 10, 10, 5, 9, 1, 2, 9, 0], [10, 5, 7, 4, 6, 6, 7, 4, 7, 1], [4, 4, 3, 0, 3, 3, 0, 0, 10, 0]]
mostra_matriz(notas)
pesos = [1,2,3,2,1]
media=[]

#Exercicio 9

def circulo(matriz):
    raio = len(matriz)//2
    centro_x = len(matriz)//2
    centro_y = len(matriz)//2
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if (i - centro_x)**2 + (j - centro_y)**2 <= raio**2:
                matriz[i][j] = 1
    return

matriz = cria_matriz(220,220)
circulo(matriz)

plt.imshow(matriz)
plt.colorbar()
plt.show()