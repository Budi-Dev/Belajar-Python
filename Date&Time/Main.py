#!/usr/bin/python3
# Latihan Date and Time
print('\n'+"Latihan Date & Time".center(50, '=')+'\n')

import datetime as dt

print("Silahkan masukkan tanggal, bulan, dan tahun lahir anda")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")
print(f"Harinya adalah : {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal : {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_sisa_bulan = (umur_hari.days % 365) // 30
print(f"Umur anda adalah {umur_tahun} tahun, {umur_sisa_bulan} bulan")