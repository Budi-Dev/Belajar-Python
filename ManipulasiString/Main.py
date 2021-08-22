#!/usr/bin/python3

def p(object):
    print(object)

# nama_depan = "Budi"
# nama_tengah = "X"
# nama_belakang = "Sec"

# nama_depan = nama_depan + " " + "'" + nama_tengah + " " + nama_belakang
# print(nama_depan)

# # Menghitung panjang string pakai fungsi len
# print("Panjang string " + nama_depan + " = " +  str(len(nama_depan)) + " karakter")

# # Cek karakter berada dalam suatu string atau tidak
# b = "i 'X"
# status = b in nama_depan
# print("String " + b + " ada di dalam " + nama_depan + " =", str(status))

# B = "B"
# status = B not in nama_depan
# print("String " + B + " tidak ada di dalam " + nama_depan + " =", str(status))

# # Mengulangi string
# print("wk" * 10)
# print(20 * "wk")

# # indexing
# print("Index ke-10 dari " + "'"  + nama_depan + "'" + " : " + nama_depan[10])
# print("Index ke--1 dari " + "'"  + nama_depan + "'" + " : " + nama_depan[-1])
# print("Index ke--2 dari " + "'"  + nama_depan + "'" + " : " + nama_depan[-2])
# print("Index ke-[0, 3] : " + nama_depan[:])

# # item paling kecil
# print("Paling kecil: " + min(nama_depan))
# print("Paling besar: " + max(nama_depan))

# ascii_code = ord(" ")
# print("ASCII Code untuk spasi adalah: " + str(ascii_code))

# # Operator dalam bentuk method

# data = "otong surotong pararotong"
# jumlah = data.count('r')
# print("Jumlah karakter 'r' dalam " + data + " = " +  str(jumlah))


# operator dalam bentuk methods

## merubah case dari string

# merubah semua ke uppercase
print("=====Upper Case")
salam = "bro!!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)


# merubah semua ke lowercase
print("=====Lower Case")
alay = "aQyuuu KecHeee  AbiezzzZzZZ"
print("Normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan isX method

# contoh untuk pengecekan lower case 
salam = "sist"
apakah_lower = salam.islower() # return bool
print(salam + " is lower case = " + str(apakah_lower))
apakah_upper = salam.isupper()
print(salam + " is upper case = " + str(apakah_upper))

def pt(object):
    print(object)

pt(salam + " is uppper case = " + str(apakah_upper))

# isalpha() => Untuk mengecek semua huruf
# isalnum() => huruf dan angka
# isdecimal() => angka saja
# isspace() => spasi, tab, newline \n
# istitle => semua kata dimulai dengan huruf besar

judul = "It's Okay Not To And Be Orkay"
cek_judul = judul.istitle() # return bool

p(judul + " adalah judul = " + str(cek_judul))

# ngecek komponen startswith dan endswtih
cek_start = "Budi Setiawan".startswith("Bu")
p("Start = " + str(cek_start))

cek_end = "Ika Cahyani".endswith("ni")
p("End = " + str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku', 'sayang', 'kamu']
gabungan = ','.join(pisah)
p(pisah)
p(gabungan)

gabungan = ' '.join(pisah)
p(gabungan)

gabungan = ' ehm '.join(pisah)
p(gabungan)

gabungan = 'akuehmsayangehmkamu'
p(gabungan.split('ehm'))

# alokasi karakter rjust(), ljust(), center()
print('\n' + "Alokasi Karakter".center(50, "="))
kanan = 'kanan'.rjust(10)
print("'" + kanan + "'")

kiri = 'kiri'.ljust(10)
print("'" + kiri + "'")

tengah = 'tengah'.center(20, ':')
print("'" + tengah + "'")

# kebalikan
print(kanan.strip()) # menghilangkan tanda ':'






