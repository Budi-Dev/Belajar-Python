#!/usr/bin/python3
# PR Python: 1(----0+++++5--------8+++++++11---------)
print('\n======PR Python NO.1======\n')
input_user = float(input("Masukkan angka yang lebih dari 0, kurang dari 11, dan bukan 5 ataupun 8\n:"))
is_lebih_dari_0 = input_user > 0
print('Lebih dari 0 =', is_lebih_dari_0)
is_kurang_dari_11 = input_user < 11
print('Kurang dari 11 =', is_kurang_dari_11)
kurang_dari_5 = input_user < 5
print('Kurang dari 5 =', kurang_dari_5)
is_lebih_dari_8 = input_user > 8
print('Lebih dari 8 =', is_lebih_dari_8)

correct = (is_lebih_dari_0 and is_kurang_dari_11) and (kurang_dari_5 or is_lebih_dari_8)
print('Angka yang anda masukkan:', correct)


