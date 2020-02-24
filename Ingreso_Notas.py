contador=1

notaMaySiete=0
notaMenSiete=0

while contador<=10:
    nota=int(input('Ingrese la nota'))
    if nota>=7:
        notaMaySiete=notaMaySiete+1
    else:
        notaMenSiete=notaMenSiete+1
    contador=contador+1
    
print('La cantoidad de estudintes con nota mayores a 7 son: '+str(notaMaySiete))
print|('La cantoidad de estudintes con nota menores a 7 son: '+str(notaMenSiete))
    
    
