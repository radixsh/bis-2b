# Lab 6: Succession in a marine fouling community

import math

def getDiversity(data):
    d = 1.0
    for num in data:
        term = 1 / math.pow(num, num)
        d *= term 
    return str(d) 

three_mo = [1/16, 2/16, 13/16]
six_mo = [22/50, 26/50, 2/50]
nine_mo = [1/194, 69/194, 76/194, 48/194]

print("True diversity at 3 mo: D = " + getDiversity(three_mo))
print("True diversity at 6 mo: D = " + getDiversity(six_mo))
print("True diversity at 9 mo: D = " + getDiversity(nine_mo))
