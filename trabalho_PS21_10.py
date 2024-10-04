##12311ECP002

def cSimilaridade(quadrado1,quadrado2):
    similar=0
    total=0
    for i in range(len(quadrado2)):
        for j in range(len(quadrado2[i])):
            total+=1
            if quadrado1[i][j] == quadrado2[i][j]:
                similar+=1
    return similar/total


def posSim(quadrado1,quadrado2):
    simMax=0
    posicaoMax=(0,0)
    n=len(quadrado1)
    m=len(quadrado2)

    for i in range(n-m+1):
        for j in range(n-m+1):
            quadradoAuxiliar=[linha[j:j+m] for linha in quadrado1[i:i+m]]
            similaridade= cSimilaridade(quadradoAuxiliar,quadrado2)
            if similaridade>simMax:
                simMax=similaridade
                posicaoMax=(i,j)
    return simMax*100,posicaoMax


n=int(input()) #entrada 1
quadrado1 = [list(map(int,input().split())) for _ in range(n)]
#print(m)

#for linha in quadrado1:
    #print(linha)


m=int(input()) #entrada2
quadrado2 = [list(map(int,input().split())) for _ in range(m)]
# for linha in quadrado2:
#     print(linha)

simMax,posicao1,posicao2=posSim(quadrado1,quadrado2)
print("Posição: ({},{})".format(posicao1,posicao2))
print("Similaridade máxima: {:.2f}%".format(simMax))