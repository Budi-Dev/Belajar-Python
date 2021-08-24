#!/usr/bin/python3
# Date and Time (latihan)

import datetime as dt

hari_ini = dt.date.today()

print(hari_ini)
print(f"Hari ini adalah hari = {hari_ini:%A}")

tanggal = dt.date(2005, 8, 10)
print(tanggal)
print(f"Hari itu adalah hari = {tanggal:%A}")