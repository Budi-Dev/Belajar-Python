# !/usr/bin/python3
# Membuat program untuk koversi celsius ke suhu lainnya

print('\n=====Selamat Datang di Alat Pengkoversi Celsius=====\n')

# Tangkap masukkan dalam suhu Celsius 
celsius = float(input("Masukkan suhu dalam celsius: "))
# Tampilkan suhu dalam celsius
print('Suhu dalam celsius adalah ' + str(celsius) + ' Derajat\n')
# Tampilkan suhu dalam Reamur90
reamur = 4 / 5 * celsius
print("Suhu dalam Reamur adalah " + str(reamur) + ' Derajat')
# Tampilkan suhu dalam fahrenheit
fahrenheit = (9 / 5 * celsius) + 32
print("Suhu dalam Farenheit adalah " + str(fahrenheit) + ' Derajat')
# Tampilkan suhu  dalam Kelvin
kelvin = celsius + 273
print("Suhu dalam Kelvin adalah " + str(kelvin) + ' Derajat')

# Close Program
print("\n=====Program Selesai Dijalankan=====\n")