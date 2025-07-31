# ELIF ADALAH CODE YANG DAPAT MEMBUAT IF MENJADI SATU BLOCK IF
menu_pilihan = input("Masukan nomor [1-3]: ")

if menu_pilihan ==  "1": # SAMPAI ELSE DI BAWAH DINAMAKAN SATU BLOCK IF
  print("Memilih nomor 1")
elif menu_pilihan == "2":
  print("Memilih nomor 2")
elif menu_pilihan == "3":
  print("Memilih nomor 3")
else:
  print("Nomor tidak terdaftar")