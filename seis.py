# -*- coding: utf-8 -*-
a= input('Digite el primer numero ')
b= input('Digite el segundo numero ')
c= input('Digite el tercer numero ')

if  a<b<c  or c<b<a:
    print("El del medio es: {}".format(b))
elif b<a<c or c<a<b:
    print("El del medio es: {}".format(a))
else:
    print("El del medio es: {}".format(c))  