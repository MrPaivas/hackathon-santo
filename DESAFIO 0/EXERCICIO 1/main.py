# HACKATHON SANTO MAIO 2023
# DESAFIO 0, EXERCÍCIO 1
# CANDIDATO: TIAGO SOUZA PAIVA

def print_asterisco(n):
    """Retorna uma lista de contagem de '*' em relação à um inteiro """
    lista = []
    for x in range(1, n+1):
        caracter = '*' * x
        lista.append(caracter)
    print(lista)


if __name__ == '__main__':
    print_asterisco(7)