def calculate_similarity(square1, square2):
    # Função para calcular a similaridade entre dois quadrados
    similar = 0
    total = 0
    for i in range(len(square2)):
        for j in range(len(square2[i])):
            total += 1
            if square1[i][j] == square2[i][j]:
                similar += 1
    return similar / total

def find_max_similarity_position(square1, square2):
    max_similarity = 0
    max_position = (0, 0)
    
    n = len(square1)
    m = len(square2)
    
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            sub_square = [row[j:j+m] for row in square1[i:i+m]]
            similarity = calculate_similarity(sub_square, square2)
            if similarity > max_similarity:
                max_similarity = similarity
                max_position = (i, j)
    
    return max_similarity * 100, max_position

# Leitura das entradas
n = int(input())
square1 = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
square2 = [list(map(int, input().split())) for _ in range(m)]

# Encontrar a posição de maior similaridade
max_similarity, position = find_max_similarity_position(square1, square2)

# Saída formatada
print("Posição:", position)
print(f"Similaridade máxima: {max_similarity:.2f}%")
