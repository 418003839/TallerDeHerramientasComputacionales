# -*- coding: utf-8 -*-
# Jorge S- Martínez Villafan
print 34*3 - 1/2 *9.8*3**2 #1/2 calcula la division entera
print 34*3 - 1.0/2 *9.8*3**2 #1.0/2 división flotante "real"

print 34*1 - 1.0/2 *9.8*1**2

print 34*1.5 - 1.0/2 *9.8*1.5**2

print 34*5 - 1.0/2 *9.8*5**2

v0 = 34
g = 9.81
t = 5
y = v0*t - 1.0/2*g*t**2
print y
