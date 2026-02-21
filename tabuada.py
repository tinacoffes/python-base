#!/usr/bin/env python
""" Imprime a Tabuada do 1 ao 10.

--Tabuada do 1--
    1 * 1 = 1
    1 * 2 = 2
    1 * 3 = 3 
. . . 

###################

--Tabuada do 2--
    2 * 1 = 2
    2 * 2 = 4
    2 * 3 = 6  
. . . 

##################
"""

__version__ = "0.1.0"
__author__ = "tina"

#number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))

#Iterable(percorriveis)

for n1 in numeros:
    print("{:-^18}".format(f"\U0001F438 Tabuada do {n1}!"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} * {n2} = {resultado}"))
    print("#" * 18)

