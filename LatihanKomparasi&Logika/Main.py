#!/usr/bin/python3

# Latihan komparasi dan operasi logika di python
print('\n=====Belajar Komparasi Dan Operasi Logika=====\n')

# Membuat gabungan area rentang dari angka

print('=====Operasi Gabungan Area======')
# ++++++++++3-------10+++++++++++
input_user = float(input("Masukkan angka yang bernilai \nkurang dari 3 \natau \nlebih dari 10\n:"))

# ++++++3------
# Memeriksa angka kurang dari 3
is_kurang_dari = input_user < 3
print('Kurang dari 3 =', is_kurang_dari)

# ------------10++++++
# Memeriksa angka lebih dari 10
is_lebih_dari = input_user > 10
print('Lebih dari 10 =', is_lebih_dari)

is_correct = is_lebih_dari or is_kurang_dari
print('Angka yang anda masukkan =', is_correct)

# Operasi gabungan
print("\n====Operasi Irisan Area=====")
# -------3++++++10-------
input_user = float(input('Masukkan angka yang bernilai \nlebih dari 3 \ndan \nkurang dari 10\n:'))

# -----3+++++++
is_lebih_dari = input_user > 3
print('Lebih dari 3 =', is_lebih_dari)
is_kurang_dari = input_user < 10
print("Kurang dari 10 =", is_kurang_dari)

is_correct = is_lebih_dari and is_kurang_dari
print("Angka yang anda masukkan =", is_correct)

print('\nProgram Selesai Dijalankan\n')