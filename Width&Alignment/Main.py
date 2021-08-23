#!/usr/bin/python3
print('\n'+"Belajar Width & Alignment".center(50, '=')+'\n')

# Data

data_nama = "Budi Setiawan"
data_umur = 16
data_tinggi = 155
data_no_sepatu = 44

# string standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_no_sepatu}"

print("Data String".center(30, '='))
print(data_string)

# string multiline (Dengan menggunakan enter, newline, \n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_no_sepatu}"

print('\n' + "Data String".center(30, '='))
print(data_string)

# string multiline (kutip triplets)
data_string = f"""
nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_no_sepatu}
"""

print("Data String".center(30, '='))
print(data_string)

# mengatur lebar
panjang_nama = len(data_nama) + 5
data_string = f"""
nama   = {data_nama:>{panjang_nama}}
umur   = {data_umur:>{panjang_nama}}
tinggi = {data_tinggi:>{panjang_nama}}
sepatu = {data_no_sepatu:>{panjang_nama}}
"""

print("Data String".center(30, '='))
print(data_string)
