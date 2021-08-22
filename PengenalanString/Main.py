#!/usr/bin/python3
data = "Ini adalah string"
print(data)
print(type(data))

# 1. Cara membuat string

'''
    1. Menggunakan single quote '...'
    2. Menggunkan double quote "..."
'''

data = 'Menggunkan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Hallo apa kabar?"')
print("'Hallo apa kabar?'")
print("Ini adalah hari jum'at")

# 2. Menggunakan tanda |

# Membuat tanda ' menjadi string
print('Mari kita sholat jum\'at')
print('g\'day, is\'t it?')

# backslash
print('C:\\User\\Ucup')

# tab
print('Budi \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPasya, sudah sangat jauh')

# backspace
print('Budi \b\bPasya, deketan')

# Multiple line string
print(
    '''
Nama     : Budi Setiawan
No       : 2
Kelas    : X SIJA 1
Angkatan : 0'25
Status   : Jomblo
    '''
)

# raw string
print(r'C:\User\I\t\n\n\n\\r\e\r\bka\Cinta')