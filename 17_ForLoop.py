pelanggan = ["eko", "budi", "joko", "andi"] 

# DALAM PERINTAH FOR LOOOP SAAT INGIN MEMANGIL DATA DARI LIST TIDAK HARUS MENULISKAN CODE SEBANYAK DIBAWAH
# print(pelanggan[0])
# print(pelanggan[1])
# print(pelanggan[2])
# print(pelanggan[3])

pelanggan.remove("eko") # SEMISAL DATA DALAM LIST DIHAPUS HASIL FOR AKAN MENGIKUTI PERINTAH YANG DITULISKAN

# CONTOH PENERAPAN PERINTAH FOR
for nama in pelanggan: # DI SINI VARIABEL NAMA AKAN MENAMPUNG DATA LIST DARI PELANGGAN
  print( f"nama pelanggan: {nama}") # SETELAH DI PANGGIL VARIABEL NAMA AKAN MEMUNCULKAN DATA LIST DARI PELANGGAN