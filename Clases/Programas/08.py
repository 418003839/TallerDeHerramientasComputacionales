#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
"""
 Jorge S Martínez Villafan, 418003839
 Herramientas computacionales
 Lo que nos explico el miercoles
"""
x = 10.5;y = 1.0/3;z = 15.3
H = """
El punto de R3 es:
(x,y,z)=(%.2f,%g,%G)
""" % (x,y,z)
print H

G="""
El punto en R3 es:
(x,y,z)=({laX:.2f}.{laY:g},{laZ:G})
""".format(laX=x,laY=y,laZ=z)

print G

import math as m
from math import sqrt
from math import sqrt as s
from math import *
x=16
x=input("Cuál es el valor al que le quieres\n" + "calcular la raíz")
print "La raiz cuadrada de %.2f es %f" % (x,m.sqrt(x))
print sqrt(16.5)
print s(16.5)
