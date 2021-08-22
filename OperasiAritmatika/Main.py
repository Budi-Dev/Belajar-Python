# Operasi Aritmatika

a = 24
b = 4

# operasi tambah +
hasil = a + b
print(a, '+', b, ' = ', hasil)

# operasi pengurangan -
hasil = a - b
print(a, '-', b, ' = ', hasil)

# operasi perkalian *
hasil = a * b
print(a, '*', b, ' = ', hasil)

# operasi pembagian /
hasil = a / b
print(a, '/', b, ' = ', hasil)

# operasi eksponen (Pangkat) **
hasil = a ** b
print(a, '**', b, ' = ', hasil)

# operasi modulus %
hasil = a % b
print(a, '%', b, ' = ', hasil)

# operasi flooe divison //
hasil = a // b
print(a, '//', b, ' = ', hasil)

# prioritas operasi / operatonal precedence

x = 3
y = 4
z = 2

hasil = x + y * z
print(x, '+', y, '*', z, ' = ', hasil)
hasil = (x + y) * z
print('(', x, '+', y, ')', '*', z, ' = ', hasil)