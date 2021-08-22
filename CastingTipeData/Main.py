# Kita belajar Casting
# Merubah dari satu tipe ke tipe lain
# tipe data = int, float, str, bool

print("=====Belajar Casting Tipe Data di Python=====\n")

## INTEGER
print('===INTEGER===')
data_int = -1
print("data = ", data_int, ', bertipe ', type(data_int))

data_float = float(data_int)
print("data = ", data_float, ', bertipe ', type(data_float))
data_str = str(data_int)
print("data = ", data_str, ', bertipe ', type(data_str))
data_bool = bool(data_int) # akan 0 jika nilai int = 0
print("data = ", data_bool, ', bertipe ', type(data_bool))

print('\n')

## FLOAT
print('===FLOAT===')
data_float = 9.8
print("data = ", data_float, ', bertipe ', type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float) # akan 0 jika nilai int = 0
print("data = ", data_int, ', bertipe ', type(data_int))
print("data = ", data_str, ', bertipe ', type(data_str))
print("data = ", data_bool, ', bertipe ', type(data_bool))
# akan false jika float = 0

print('\n')

## BOOLEAN
print('===BOOLEAN===')
data_bool = False
print("data = ", data_bool, ', bertipe ', type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool) # akan 0 jika nilai int = 0
print("data = ", data_int, ', bertipe ', type(data_int))
print("data = ", data_str, ', bertipe ', type(data_str))
print("data = ", data_float, ', bertipe ', type(data_float))

print('\n')

## STRING
print('===STRING===')
data_str = ""
print("data = ", data_str, ', bertipe ', type(data_str))

# data_float = float(data_str) # String harus angka
# data_int = int(data_str) # String harus angka
data_bool = bool(data_str) # akan 0 jika string sama dengan kosong
print("data = ", data_float, ', bertipe ', type(data_float))
print("data = ", data_int, ', bertipe ', type(data_int))
print("data = ", data_bool, ', bertipe ', type(data_bool))