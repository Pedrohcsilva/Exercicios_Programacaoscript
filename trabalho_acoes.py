#lucro é oq conseguiu com as vendas
N=int(input("numero de dias que tenho o preço das acoes? ".upper()))
lista=[]
l=0

for i in range(N):
    lista.append(float(input("valores das acoes: ".upper())))

k=int(input("dias permitidos entre a compra e a venda das acoes: "))
q=int(input("quantidade de dinheiro levada: "))

for i in range(len(lista)):
    for j in range(i,i+k):
        qtdComprada=q//lista[i]
        totalGasto=qtdComprada*lista[i]
        totalVendido=qtdComprada*lista[j]
        lucroobtido=totalVendido+(q%k)-k
        if lucroobtido>l:
            diaCommpra=k
            diaVenda=k+lista[i]
            
            



print("Dia de compra: {}".format(diaCompra))
print("Valor de compra: R$", format(precoCompra, '.2f'))
print("Dia de venda: {}".format(diaVenda))
print("Valor de venda: R$", format(precoVenda, '.2f'))
print("Quantidade comprada: {}".format(qtdcomprada))
print("Lucro: R$", format(lucro, '.2f'))