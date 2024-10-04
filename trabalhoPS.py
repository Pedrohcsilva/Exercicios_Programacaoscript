#12311ECP002
#Pedro Henrique Silva##

def horizontal(p):
    cont = 0
    for i_linha in range(linhas):
        for i_coluna in range(colunas - len(p) + 1):
            check = 0
            for j in range(len(p)):
                if matrix[i_linha][i_coluna + j].lower() == p[j].lower() or matrix[i_linha][i_coluna + j] == '*':
                    check += 1

            if check == len(p):
                cont += 1
                for k in range(len(p)):
                    matrix[i_linha][i_coluna + j - k] = matrix[i_linha][i_coluna + j - k].upper()
    return cont

def vertical(p):
    cont = 0
    for i_coluna in range(colunas):
        for i in range(linhas - len(p) + 1):
            check = 0
            for j in range(len(p)):
                if matrix[i + j][i_coluna].lower() == p[j].lower() or matrix[i + j][i_coluna] == "*":
                    check += 1

            if check == len(p):
                cont += 1
                for k in range(len(p)):
                    matrix[i + j - k][i_coluna] = matrix[i + j - k][i_coluna].upper()
    return cont

def diagonal_1(p):
    cont = 0
    for i_coluna in range(colunas - len(p) + 1):
        for i_linha in range(linhas - len(p) + 1):
            check = 0
            for j in range(len(p)):
                if matrix[i_linha + j][i_coluna + j].lower() == p[j].lower() or matrix[i_linha + j][i_coluna + j] == "*":
                    check += 1
            if check == len(p):
                cont += 1
                for k in range(len(p)):
                    matrix[i_linha + j - k][i_coluna + j - k] = matrix[i_linha + j - k][i_coluna + j - k].upper()
    return cont

def diagonal_2(p):
    cont = 0
    for i_coluna in range(colunas - len(p) + 1):
        for i_linha in range(len(p) - 1, linhas):
            check = 0
            for j in range(len(p)):
                if matrix[i_linha - j][i_coluna + j].lower() == p[j].lower() or matrix[i_linha - j][i_coluna + j] == "*":
                    check += 1
            if check == len(p):
                cont += 1
                for k in range(len(p)):
                    matrix[i_linha - j + k][i_coluna + j - k] = matrix[i_linha - j + k][i_coluna + j - k].upper()
    return cont

linhas = int(input())
colunas = int(input())
matrix = []
for i in range(linhas):
    matrix.append(input().split())

palavras = []
for i in range(int(input())):
    palavras.append(input())

# Contabiliza e destaca as palavras encontradas na nota
resultados = []
print("----------------------------------------")
print("Lista de Palavras")
print("----------------------------------------")
for i in range (len(palavras)):
    contagem = 0
    contagem += horizontal(palavras[i])
    contagem += vertical(palavras[i])
    contagem += diagonal_1(palavras[i])
    contagem += diagonal_2(palavras[i])
    print("Palavra:",palavras[i])
    print("Ocorrencias:",contagem)
    print("----------------------------------------")

# Imprime a nota destacando as palavras encontradas
for linha in matrix:
    print(" ".join(linha))
