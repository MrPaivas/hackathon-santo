from random import randint


# HACKATHON SANTO MAIO 2023
# DESAFIO 0, EXERCÍCIO 2
# CANDIDATO: TIAGO SOUZA PAIVA
lista = []


def gera_lista():
    """Essa função gera uma lista com valores aleatórios com 7 inteiros"""
    for x in range(1, 7+1):
        lista.append(randint(1, 1000)) # lista com 7 inteiros de 1 até 1000
    print(lista)


def menor_diferenca(lista):
    """Essa função deve retornar o par de números coma menor diferença absoluta"""
    lista_ordenada = sorted(lista)
    menor_diferenca = 1001  # variavel recebe valor da maior diferença possivel para primeira compraração
    pares = []

    for x in range(len(lista_ordenada) - 1):
        diferenca = abs(lista_ordenada[x] - lista_ordenada[x + 1])

        if diferenca < menor_diferenca:
            menor_diferenca = diferenca
            pares = [(lista_ordenada[x], lista_ordenada[x + 1])]
        elif diferenca == menor_diferenca:
            pares.append((lista_ordenada[x], lista_ordenada[x + 1]))

    print(pares)


if __name__ == '__main__':
    print("A lista analizada é:")
    gera_lista()
    print('E os numeros mais próximos são:')
    menor_diferenca(lista)