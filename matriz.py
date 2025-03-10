import matplotlib.pyplot as plt
matriz = [[1,2,3],[4,5,6],[7,8,9]]

#plt.imshow(matriz,'hot')
#plt.colorbar()
#plt.show()




#for i in range(len(matriz)):
#    for num_mat in matriz:
#        print(matriz)


#def elementos(matriz):
#    for i in range(len(matriz)):
#        for j in range(len(matriz[i])):
#            print(matriz[i][j])
#    return

def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)
    return




def cria_matriz(matriz_row, matriz_column):
    matriz_nova = []
    for i in range(matriz_row):
        matriz_sub = []
        for j in range(matriz_column):
            matriz_sub.append(0)
        matriz_nova.append(matriz_sub)
    return matriz_nova


"""matriz_nova = []
for i in range(matriz_row):
    matriz_sub = []
    for j in range(matriz_column):
        if j > i:
            matriz_sub.append(j+i)
        else:
            matriz_sub.append(j)
    matriz_nova.append(matriz_sub)
print(matriz_nova)

"""

"""matriz = cria_matriz(10,10)
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == j:
            matriz[i][j] = 1
for i in range(len(matriz)):
    matriz[i][i] = 1"""

def contra_diagonal(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i + j == len(matriz) - 1:
                matriz[i][j] = 1

def contra_diagonal(matriz):
    for i in range(len(matriz)):
        matriz[i][len(matriz) - 1] = 1
    return


"""def chess_board(chess_matriz):
    for i in range(len(chess_matrix)):
        for j in range(len(chess_matrix)):
            if i%2 == 0:
                if j % 2 == 0:
                    chess_matrix[i][j] = 0
                else:
                    chess_matrix[i][j] = 1
            else:
                if j % 2 == 0:
                    chess_matrix[i][j] = 1
                else:
                    chess_matrix[i][j] = 0
    return
"""

"""
chess_matrix = cria_matriz(8,8)

def chess_board(chess_matrix):
    for i in range(len(chess_matrix)):
        for j in range(len(chess_matrix)):
            if (i+j)%2== 0:
                chess_matrix[i][j] = 1
            else:
                chess_matrix[i][j] = 0
    return
"""

    





plt.imshow()
plt.colorbar()
plt.show()

