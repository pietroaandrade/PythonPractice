makes = {
    "makes" : ["base", "blush", "rimel", "sombra", "batom"],
    "estoque" : [2,4,6,8,10]
}


indices = {makes["makes"][i] : i for i in range(len(makes["makes"])) }
def estoque(dic):
    make = input("Qual maquiagem voce quer?")
    qtd = int(input("quantas makes voce quer?"))

    indice_produto = indices[make]

    if qtd > dic["estoque"][indice_produto]:
        print("erro")
    else:
        dic["estoque"][indice_produto] -= qtd

        print(dic["estoque"])
    return


estoque(makes)