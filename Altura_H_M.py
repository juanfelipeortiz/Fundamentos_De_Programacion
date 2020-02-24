name='' 
gen=''
alt=0

TtlHom=0
TtlMuj=0

sumAltGnr=0
sumAltHom=0
sumAltMuj=0

promAltGnr=0
promAltHom=0
promAltMuj=0

contador=1
cantPer=0

cantPer=int(input('Ingrese la cantidad de personas: '))

while contador<=cantPer:
    name  =input('Ingrese el nombre: ')
    gen   =input('Ingrese el genero, si es hombre utiliza H, si es mujer utiliza M: ')
    alt   =float(input('Ingrese la altura: '))
    
    sumAltGnr=sumAltGnr+alt
    
    if gen=='H':
        sumAltHom=sumAltHom+alt
        TtlHom=TtlHom+1
    else:
        sumAltMuj=sumAltMuj+alt
        TtlMuj=TtlMuj+1
    
    contador=contador+1
    
promAltGnr=sumAltGnr/cantPer
promAltMuj=sumAltMuj/TtlMuj
promAltHom=sumAltHom/TtlHom
print('El promedio de la altura general es: '+str(promAltGnr))
print('El promedio de la altura de las mujeres es: '+str(promAltMuj))
print('El promedio de la altura de los hombres es: '+str(promAltHom))
