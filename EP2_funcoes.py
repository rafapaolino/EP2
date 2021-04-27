#funcoes dos exercicios na academia

# devolve uma lista de cartas em um baralho

def cria_baralho():
    listaM = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    listar = []
    for i in listaM:
        listar.append(str(i) + "♦")
        listar.append(str(i) + "♠")
        listar.append(str(i) + "♥")
        listar.append(str(i) + "♣")
    return listar



# recebe carta devolve naipe

def extrai_naipe(carta):
    return carta[-1]



# recebe carta devolve valor

def extrai_valor(carta):
    return carta[:-1]



# recebe um baralho (lista) e o indice de uma carta, devolve movimentos possiveis,
# sendo 1 = pode ser empilhada no vizinho anterior e 3 = pode ser empilhado no terceiro
# vizinho antes

def lista_movimentos_possiveis(baralho, i):
    carta = baralho[i]
    if i > 0:
        v1 = baralho[i-1]
    if i > 2:
        v3 = baralho[i-3]
    if i - 3 < 0:
        p3 = False
    elif extrai_naipe(carta) == extrai_naipe(v3) or extrai_valor(carta) == extrai_valor(v3):
        p3 = True
    else:
        p3 = False
    if i - 1 < 0:
        p1 = False
    elif extrai_naipe(carta) == extrai_naipe(v1) or extrai_valor(carta) == extrai_valor(v1):
        p1 = True
    else:
        p1 = False
    
    listar = []
    if p1 and p3:
        listar = [1, 3]
    elif p1:
        listar = [1]
    elif p3:
        listar = [3]
    
    return listar



# recebe baralho, i-origem e i-destino e devolve novo baralho

def empilha(baralho, io, id):
    baralho[id] = baralho[io]
    del baralho[io]
    return baralho



# recebe baralho, devolve T/F se existem movimentos possiveis

def possui_movimentos_possiveis(baralho):
    for i in range(len(baralho)):
        mp = lista_movimentos_possiveis(baralho, i)
        if not mp == []:
            return True
    return False

