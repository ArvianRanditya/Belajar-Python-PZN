nama_depan = "Budi"
nama_tengah = "Susanto"
nama_belakang = "Eko"
# UNTUK PENULISAN FORMAT STRING SEPERTI BERIKUT SANGAT MELELAHKAN DAN TIDAK EFISIEN
sapa = "Hallo " + nama_depan + " " + nama_tengah + " " + nama_belakang
print(sapa)

# PENULISAN STRING FORMAT YANG LEBIH BAIK
sapa = f"Hallo {nama_depan} {nama_tengah} {nama_belakang}" # TAMBAHKAN HURUF f UNTUK MENJALANKAN FORMAT STRING
print(sapa)