#Pedro Henrique de Casto Silva ###### 12311ECP002
#########################################################
v=int(input())
d=int(input())
i=1
horas_trabalhadas=0
hora_extra=0                    #variaveis
valor_devido=0
while(i<=d):
    periodos=int(input()) #periodos
    i+=1
    while(periodos>0):
        hi=int(input()) #hora de inicio
        hf=int(input()) #horas fim
        horas_trabalhadas=horas_trabalhadas+(hf-hi)
        if(hf-hi>8):
            hora_extra=(hf-hi)-8+hora_extra
            if(hora_extra>10):
              valor_devido=(v*1.5)*hora_extra+(horas_trabalhadas-hora_extra)*v
              
        elif(horas_trabalhadas-hora_extra>44):
            hora_extra=horas_trabalhadas-44
            valor_devido=(v*1.5)*hora_extra+(horas_trabalhadas-hora_extra)*v
        elif(hora_extra>0):
            valor_devido=(v*1.5)*hora_extra+(horas_trabalhadas-hora_extra)*v
        else:
            valor_devido=horas_trabalhadas*v
        periodos-=1

print(f'Horas trabalhadas: {horas_trabalhadas}')
print(f'Horas extras: {hora_extra}')
print('Valor devido: R$ {:.2f}'.format(valor_devido))