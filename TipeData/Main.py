print("\n===== Belajar Tipe Data di Python =====")
# a = 10, a adalah variabel dengan nilai 10

# tipe data: Angka Satuan yang tidak ada komanya (integer)
data_integer = 2980398
print("\nData: " + str(data_integer) + ', bertipe: ' + str(type(data_integer)));

# tipe data: Angka dengan pecahan (float)
data_float = 3 * 10**2
print("\nData: " + str(data_float) + ', bertipe: ' + str(type(data_float)));

# tipe data: Kumpulan karakter (string)
data_string = "Si Ucup 224"
print("\nData: " + str(data_string) + ', bertipe: ' + str(type(data_string)));

# tipe data: Biner true / false (Boolean)
data_bool = False
print("\nData: " + str(data_bool) + ', bertipe: ' + str(type(data_bool)));

## Tipe data khusus

# bilangan kompleks
data_complex = complex(5, 6)
print("\nData: " + str(data_complex) + ', bertipe: ' + str(type(data_complex)));

# tipe data dari bahasa C
from ctypes import c_double
data_c_double = c_double(10.55)
print("\nData: " + str(data_c_double) + ', bertipe: ' + str(type(data_c_double)));
 