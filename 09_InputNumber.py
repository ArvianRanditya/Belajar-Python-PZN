print("Masukan nilai a : ")
a = int( input() ) # MENAMBAHKAN int() DIKARENAK NILAI INPUT SELALU STRING MAKA DI KONVERSI KE INT

print("Masukan nilai b : ")
b = int( input() )

hasil = a + b
print( f"{a} + {b} = {hasil}" ) # JIKA TIDAK MENGGUNAKAN int() MAKA JIKA NILAI a=5 DAN b=5 HASILNYA AKAN 55