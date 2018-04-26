#  -*- coding: utf8 -*-
estado = input('digite 1 para dormir y 2 para resposo')
horas = input ('digite el numero de minutos que realizo la activida')
if estado==1:
    calorias=horas*1.08
    print('las calorias quemadas son: {0}'.format(calorias))
else:
    calorias=horas*1.63
    print('las calorias quemadas son: {0}'.format(calorias))    