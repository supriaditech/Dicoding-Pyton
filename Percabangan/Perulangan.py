# contoh for
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in angka:
#     print(i)

# for a in range(1,22, 10):
#     print("Ini adalah pengguanaan range",a)

# contoh for bersarang
# contoh for bersarang (inner loop dan outer loop)
namaUser = [
    "supriadi",
    "icha",
    "budi",
    "agus",
    "bambang",
    "koji",
    "yanto",
    "narto",
    "indar",
    "joko",
]

# outer loop
# for k in angka:
#     # inner loop
#     for j in namaUser:
#         print(f"{k} {j}") # print output dari inner loop dan outer loop

# penjelasan:
# 1. outer loop akan dijalankan dulu
# 2. inner loop akan dijalankan di dalam outer loop
# 3. inner loop akan dijalankan sebanyak outer loop
# 4. output dari inner loop akan di print di dalam outer loop
# 5. output dari outer loop akan di print di luar inner loop

# contoh penggunaan break
# for i in range(2):  # Perulangan tingkat pertama
#     print("Perulangan luar:", i)
#     for j in range(10):  # Perulangan tingkat kedua
#         print("Perulangan dalam:", j)
#         if j == 1:
#             break  # Menghentikan perulangan dalam jika j = 1

# for huruf in "supriadi":
#     if huruf == "i":
#         break
#     print("Huruf:", huruf)
# for huruf in "supri adi":
#     if huruf == " ":
#         continue
#     print("Huruf:", huruf)

# penggunaan else pada perulangan
# for nama in namaUser:
#     if nama == "agung":
#         print("Nama ditemukan")
#         break
#     else:
#         print("Tidak ditemukan")

# penggunaan else pada while
# angkaSpesial = 0
# while angkaSpesial < 10:
#     print("Angka spesial:", angkaSpesial)
#     angkaSpesial += 1
# else:
#     print("Selesai")

# pengguanaan break pada while
# nomor = 9
# while nomor > 0:
#     nomor= nomor - 1
#     if nomor == 5:
#         break
#     print(nomor)
# else:
#     print("Selesai")

# contoh pengguaan while
# counter = 1
# while counter <= 5:
#     print(counter)
#     counter += 1


# List Comprehension
# pangkat=[]
# for nilai in angka:
#     pangkat.append(nilai**2)
# print(pangkat)

# contoh lain
# List Comprehension
# pangkat = [n**2 for n in angka]
# print(pangkat)

# Penjelasan:
# 1. List Comprehension adalah fitur Python yang memungkinkan kita membuat list baru dengan mudah dan lebih singkat.
# 2. List Comprehension menggunakan sintaks "[ekspresi for item in iterable]"
# 3. List Comprehension akan menghasilkan list baru yang berisi hasil ekspresi yang dijalankan untuk setiap item dalam iterable.
# 4. List Comprehension dapat digunakan untuk menggantikan perulangan for yang berisi append().
# 5. List Comprehension juga dapat digunakan untuk menggantikan perulangan for yang berisi if.
pangkat = [n**2 for n in angka]
print(pangkat)
