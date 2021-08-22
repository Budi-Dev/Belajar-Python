#!/usr/bin/python3
print('\n=====Belajar Operasi Komparasi di Python=====')

# operasi komparasi

# setiap hasil dari operasi komparasi adalah boolean

# operator: >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# lebih besar dari >
print('\n======== Lebih Besar Dari (>)')
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = b > 2
print(b, '>', 2, '=', hasil)

# kurang dari
print('\n======== Kurang Dari (<)')
# lebih besar dari <
hasil = a < 3
print(a, '<', 3, '=', hasil)
hasil = b < 3
print(b, '<', 3, '=', hasil)
hasil = b < 2
print(b, '<', 2, '=', hasil)

# lebih besar dari sama dengan
print('\n======== Lebih Besar Dari Sama Dengan (>=)')
hasil = a >= 3
print(a, '>=', 3, '=', hasil)
hasil = b >= 3
print(b, '>=', 3, '=', hasil)
hasil = b >= 2
print(b, '>=', 2, '=', hasil)

# kurang dari sama dengan
print('\n======== Kurang Dari Sama Dengan (<=)')
hasil = a <= 3
print(a, '<=', 3, '=', hasil)
hasil = b <= 3
print(b, '<=', 3, '=', hasil)
hasil = b <= 2
print(b, '<=', 2, '=', hasil)

# sama dengan
print('\n======== Sama Dengan (==)')
hasil = a == 4
print(a, '==', 4, '=', hasil)
hasil = a == 2
print(a, '==', 2, '=', hasil)

# tidak sama dengan
print('\n======== Tidak Sama Dengan (!=)')
hasil = a != 4
print(a, '!=', 4, '=', hasil)
hasil = a != 2
print(a, '!=', 2, '=', hasil)

print('\n')

# 'is' sebagai komparasi object identity
print('\n======== Object Identity (is)')
x = 5 # ini adalah assigment membuat object
y = 5
print('Nilai x =', x, ', id =', hex(id(x)))
print('Nilai y =', y, ', id =', hex(id(y)))
hasil = x is 5
print('x is 5 =', hasil)

x = 5 # ini adalah assigment membuat object
y = 6
print('Nilai x =', x, ', id =', hex(id(x)))
print('Nilai y =', y, ', id =', hex(id(y)))
hasil = x is y
print('x is y =', hasil)

# 'is not' sebagai komparasi object identity
print('\n======== Object Identity (is not)')
x = 5 # ini adalah assigment membuat object
y = 5
print('Nilai x =', x, ', id =', hex(id(x)))
print('Nilai y =', y, ', id =', hex(id(y)))
hasil = x is not 5
print('x is not 5 =', hasil)

x = 5 # ini adalah assigment membuat object
y = 6
print('Nilai x =', x, ', id =', hex(id(x)))
print('Nilai y =', y, ', id =', hex(id(y)))
hasil = x is not y
print('x is not y =', hasil)

























