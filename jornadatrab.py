#Pedro Henrique de Casto Silva //// 12311ECP002


#tempo de trqbalho e valor a receber.

v=int(input()) #valor da hora de trabalho
d=int(input()) #dias trabalhados
horas_trabalhadas=0
hora_extra=0
valor_devido=0
i=1

while(i<=d):
    np=int(input()) #periodos
    hi=int(input()) #hora de inicio
    hf=int(input()) #horas fim
    horas_trabalhadas=horas_trabalhadas+(hf-hi)
    i+=1
    if(hf-hi>8):
        hora_extra=(hf-hi)-8+hora_extra
if(hora_extra>0):
    valor_devido=(v*1.5)*hora_extra+(horas_trabalhadas-hora_extra)*v
elif(horas_trabalhadas > 44):
    hora_extra += horas_trabalhadas - 44
    horas_trabalhadas = 44
    valor_devido=(v*1.5)*hora_extra+(horas_trabalhadas-hora_extra)*v
else:
    valor_devido=horas_trabalhadas*v

print(f'Horas trabalhadas: {horas_trabalhadas}')
print(f'Horas extras: {hora_extra}')
print('Valor devido: R$ {:.2f}'.format(valor_devido))