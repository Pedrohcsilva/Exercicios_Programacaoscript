m= int(input("n de mes analisados"))
D2 = 0  #compl imuni
D1 = 0  #vaci 1 dose
D2A = 0 # tomaram a 2º com atraso
D1A = 0 #esperando a 2º dose
while (m>0):
    vacinas=int(input("n de vacianas"))
#PESSOAS 2º ATRASADA
    if (D1A>0):
        if(vacinas >= D1A):
            D2A += D1A
            vacinas -= D1A
            D1A = 0
        else:
            D2A += vacinas
            D1A -= vacinas
            vacinas = 0
#PESSOAS 1º DOSE EM DIA
    if (D1>0):
        if (vacinas >= D1):
            D2 += D1
            vacinas -= D1
            D1 = 0
        else:
            D2 += vacinas
            D1 -= vacinas
            vacinas = 0
#RESTO APLICADAS COMO PRIMEIRA DOSE
    if (vacinas > 0):
         D1 += vacinas
    m-=1

print("Pessoas completamente imunizadas:", D2)
print("Pessoas imunizadas apenas com uma dose:", D1)
print("Pessoas que tomaram a segunda dose com atraso:", D2A)
print("Pessoas esperando a segunda dose com atraso:", D1A)