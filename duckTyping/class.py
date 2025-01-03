# Class Mobil memiliki atribut bernama warna yang memiliki nilai "Merah".
# Lalu, kita membuat objek mobil_1 dari class Mobil.
# Kita dapat mengakses atribut warna dari objek mobil_1 untuk melihat nilainya.
# class Mobil:
#     # Atribut
#     warna = "Merah"

# mobil_1 = Mobil()
# print(mobil_1.warna)
# Mobil.warna = "putih"
# print(mobil_1.warna)

# class Mobil:
#     """
#     Class constructor Mobil ini memiliki parameter self yang merupakan referensi ke objek yang dibuat.
#     Pada saat objek dibuat, atribut warna diinisialisasi dengan nilai 'Merah'.
#     """
#     def __init__(self):
#         self.warna = 'Merah'


# mobil_1 = Mobil()
# mobil_2 = Mobil()

# print(mobil_1.warna)
# print(mobil_2.warna)

# # Mengubah atribut instance
# mobil_1.warna = "Hitam"

# # Menampilkan kembali atribut warna
# print(mobil_1.warna)
# print(mobil_2.warna)


# class Mobil:
#     def __init__(self, warna, merek, kecepatan):
#         self.warna = warna
#         self.merek = merek
#         self.kecepatan = kecepatan

# mobil_1 = Mobil('Merah', 'DicodingCar', 160)

# print(mobil_1.warna)
# print(mobil_1.merek)
# print(mobil_1.kecepatan)


# # methoddef
# def my_decorator(func):
#     def wrapper():
#         print("Sebelum fungsi dieksekusi.")
#         func()
#         print("Setelah fungsi dieksekusi.")
#     return wrapper
# # Dekorasi fungsi dengan decorator
# @my_decorator
# def say_hello():
#     print("Hello, world!")

# # Memanggil fungsi yang sudah didekorasi
# say_hello()


# class Mobil:
#     def __init__(self, warna, merek, kecepatan):
#         self.warna = warna
#         self.merek = merek
#         self.kecepatan = kecepatan

#     def tambah_kecepatan(self):
#         self.kecepatan += 10

# mobil_1 = Mobil("Merah", "DicodingCar", 160)
# print("Sebelum ditambahkan: ")
# print(mobil_1.kecepatan)

# mobil_1.tambah_kecepatan()        # Memanggil metode tambah_kecepatan.

# print("Setelah ditambahkan: ")
# print(mobil_1.kecepatan)


# class Mobil:
#     def __init__(self, merek):
#         self.merek = merek

#     @staticmethod
#     def intro_mobil():
#         print("Ini adalah metode dari kelas Mobil")

# Mobil.intro_mobil()
# mobil_1 = Mobil("DicodingCar")
# mobil_1.intro_mobil()


# class Mobil:
#     def __init__(self, merek):
#         self.merek = merek

#     @classmethod
#     def intro_mobil(cls):
#         print("Ini adalah metode dari kelas Mobil")

#     @classmethod
#     def intro_mobil2(*args):
#         print(args)

# Mobil.intro_mobil()
# mobil_1 = Mobil("DicodingCar")
# mobil_1.intro_mobil()
# mobil_1.intro_mobil2()


# pewarisan
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10


# class MobilSport(Mobil):
#     def turbo(self):
#         self.kecepatan += 50

# # Kelas Mobil Dasar
# mobil_1 = Mobil("Merah", "DicodingCar", 160)
# print(mobil_1.kecepatan)

# # Kelas Mobil Sport
# mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
# print(mobil_sport_1.kecepatan)
# mobil_sport_1.turbo()
# print(mobil_sport_1.kecepatan)

# overide
# class Mobil:
#     def __init__(self, warna, merek, kecepatan):
#         self.warna = warna
#         self.merek = merek
#         self.kecepatan = kecepatan

#     def tambah_kecepatan(self):     # tambah_kecepatan
#         self.kecepatan += 10

# class MobilSport(Mobil):
#     def turbo(self):
#         self.kecepatan += 50

#     def tambah_kecepatan(self):     # tambah_kecepatan
#         self.kecepatan += 20

# # Kelas Mobil Sport
# mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
# print(mobil_sport_1.kecepatan)
# mobil_sport_1.tambah_kecepatan()     # Memanggil metode baru tambah kecepatan()
# print(mobil_sport_1.kecepatan)


# Super


class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):  # tambah_kecepatan
        self.kecepatan += 10


class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50

    def tambah_kecepatan(self):  # tambah_kecepatan
        super().tambah_kecepatan()
        print("kecepatan baru: ", self.kecepatan)


# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
print(mobil_sport_1.kecepatan)
mobil_sport_1.tambah_kecepatan()  # Memanggil metode baru tambah kecepatan()
print(mobil_sport_1.kecepatan)
