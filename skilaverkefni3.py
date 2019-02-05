# Matthías Ólafur
from string import ascii_lowercase
from itertools import combinations
from time import perf_counter

def ord(fjoldiStafa):
    ordin = []
    for x in combinations(ascii_lowercase,fjoldiStafa):
        ord = ""
        for i in x:
            ord += i
        ordin.append(ord)
    return ordin
def rugla(l):
    tmp = []
    for x in range((len(l)-1),-1,-1):
        tmp.append(l[x])
    return tmp
def bubble(l):
    while True:
        clean = True
        for x in range(len(l)):
            if x == len(l) - 1:
                break
            if l[x] > l[x + 1]:
                tmp = l[x]
                l[x] = l[x + 1]
                l[x + 1] = tmp
                clean = False
        if clean:
            break

# Dæmi 4
timi = perf_counter()
ordin = ord(4)
print("Tímamæling\n",round((perf_counter()-timi)*1000,4),"ms")
print("Orðin okkar\n",ordin,"\nLengd listans\n",len(ordin))

# Dæmi 5
'''
ordin = rugla(ordin)
print("\nOrðin í rugli\n",ordin,"\nLengd listans\n",len(ordin))

bubble(ordin)
print("\nOrðin bubble sorteruð\n",ordin,"\nLengd listans\n",len(ordin))
'''