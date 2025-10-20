#!/usr/bin/env python

'''Divisió. Calcula el quocient i el residu d'una divisió entre dos nombres

Institut Icària
Programació - 1r Batxillerat - Curs 2025-26

El programa demana al usuari un dividend i un divisor, a continuació el
programa calcula i mostra el quocient i el residu de la divisió
entera entre aquests dos nombres.
'''

dividend = int(input("dividend"))
divisor = int(input("divisor"))
quocient = (dividend)//(divisor)
residu = (dividend) % (divisor)
print(f"Divisió: {dividend}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")
