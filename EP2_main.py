# definindo todas as funcoes

def cria_baralho():
    listaM = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    listar = []
    for i in listaM:
        listar.append(str(i) + "♦")
        listar.append(str(i) + "♠")
        listar.append(str(i) + "♥")
        listar.append(str(i) + "♣")
    return listar

def extrai_naipe(carta):
    return carta[-1]

def extrai_valor(carta):
    return carta[:-1]

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

def empilha(baralho, io, id):
    baralho[id] = baralho[io]
    del baralho[io]
    return baralho

def possui_movimentos_possiveis(baralho):
    for i in range(len(baralho)):
        mp = lista_movimentos_possiveis(baralho, i)
        if not mp == []:
            return True
    return False


########################


# bienvenidos

print("Bem vindo ao paciência acordeão!")
print("Neste jogo voce deve empilhar as cartas ate ter apenas uma pilha.")
print("Voce pode empilhar uma carta em seu vizinho anterior, ou na carta 3 casa antes.")
print("Para empilhar, ambas as cartas devem ter o mesmo naipe OU o mesmo valor.")

def main():
    dc = input("Comecar uma nova partida? (s/n) :")
    