#!/usr/bin/python3

print("Belajar Format String".center(50, '='))

# contoh generic
# string 
nama = "ucup"
format_str = f"Halo {nama}"
print(format_str)

# boolean
boolean = False
format_str = f"Boolean = {boolean}"
print(format_str)

# angka
angka = 2005.5
format_str = f"Angka = {angka}"
print(format_str)

# bilangan bulat 
angka = 15
format_str = f"Angka = {angka:d}"
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000000000
format_str = f"Ribuan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.564567
format_str = f"Angka = {angka:.2f}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10.87663525
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"

print(format_minus)
print(format_plus)

# memformat persen
persen = 0.045
format_persen = f"persen = {persen:.2%}"

print(format_persen)

# melakukan operasi aritmatika dalam placeholder
harga = 5000
jumlah = 5

format_string = f"Total harga = Rp. {harga*jumlah:,}"
print(format_string)

# format ke bilangan lain binary, octal, dan hexadesimal
angka = 255

format_bin = f"Binary = {bin(255)}"
format_oct = f"Octal = {oct(255)}"
format_hex = f"Hexadecimal = {hex(255)}"

print(format_bin + "\n" + format_oct + '\n' + format_hex)