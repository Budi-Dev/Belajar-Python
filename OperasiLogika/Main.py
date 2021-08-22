#!/usr/bin/python3
# operasi logika atau boolean
print("\n==========Belajar Operasi Logika di Python==========\n")
# not, or, and, xor

# NOT
print('=====NOT=====')
a = False
c = not a
print('Data a =', a)
print('-------- NOT')
print('Data c =', c)
# OR (Jika salah satu true, maka hasilnya true)
print('\n=====OR=====')
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = True
b = False
c = a or b
print(a, ' OR', b, '=', c)
a = False
b = True
c = a or b
print(a, 'OR', b, ' =', c)
a = True
b = True
c = a or b
print(a, ' OR', b, ' =', c)
# AND (Jika salah satu false, maka hasilnya false)
print('\n=====AND=====')
a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)
a = True
b = False
c = a and b
print(a, ' AND', b, '=', c)
a = False
b = True
c = a and b
print(a, 'AND', b, ' =', c)
a = True
b = True
c = a and b
print(a, ' AND', b, ' =', c)
# XOR (Akan true jika salah satu inputnya true, sisanya false)
print('\n=====XOR=====')
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = True
b = False
c = a ^ b
print(a, ' XOR', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'XOR', b, ' =', c)
a = True
b = True
c = a ^ b
print(a, ' XOR', b, ' =', c)


