i = 62
r = 189876545.7654675432

# Print out numbers with quotes "" such that we see the
# width of the field
print '"%d"' % i       # minimum field
# Numero entero
print '"%5d"' % i      # field of width 5 characters
# Campo con 5 caracteres de ancho
print '"%05d"' % i     # pad with zeros
# Con ceros
print '"%g"' % r       # r is big number so this is scientific notation
# Menor cantidad de carácteres
print '"%G"' % r       # E in the exponent
# E en el exponente
print '"%e"' % r       # compact scientific notation
print '"%E"' % r       # compact scientific notation
# Notación cientifica
print '"%20.2E"' % r   # 2 decimals, field of width 20
# dos decimales después
print '"%30g"' % r     # field of width 30 (right-adjusted)
#Campo de ancho 30, ajustado a la derecha
print '"%-30g"' % r    # left-adjust number
# Ajustado a la izquierda
print '"%-30.4g"' % r  # 3 decimals
#3 decimales
print '%s' % i   # can convert i to string automatically
# Muestra la cadena
print '%s' % r

# Use %% to print the percentage sign
print '%g %% of %.2f Euro is %.2f Euro' % \
      (5.1, 346, 5.1/100*346)
