# HACKATHON SANTO MAIO 2023
# DESAFIO 0, EXERCÍCIO 3
# CANDIDATO: TIAGO SOUZA PAIVA


def faz_sub_conjuntos(conjunto):
    """Essa função faz sub listas com todas as combinações possiveis com os valores de uma lista inicial"""
    sub_conjuntos = []
    conjunto_vazio = []
    sub_conjuntos.append(conjunto_vazio)  # Colocando um conjunto vazio primeiro
    for valor in conjunto: # Laço passa em todos os valores da lista de entrada
        novo_conjunto = []
        # Esse segundo laço em cada valor da lista de resposta, soma uma lista com o valor da lista de entrada
        for sub_conjunto in sub_conjuntos:
            novo_conjunto.append(sub_conjunto + [valor])
        sub_conjuntos.extend(novo_conjunto)

    print(sub_conjuntos)


if __name__ == '__main__':
    lista = [1, 2, 3]
    faz_sub_conjuntos(lista)
