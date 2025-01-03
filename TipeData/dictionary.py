"""
ictionary didefinisikan dengan kurawal dan tambahan definisi berikut.

Setiap elemen pasangan key-value dipisahkan dengan koma (,).
Key dan value dipisahkan dengan titik dua (:).
Key dan value dapat berupa tipe variabel/objek apa pun.'

"""

x = {"name": "supriadi", "age": 20, "isMarried": False}

print(type(x))

"""
Output:
<class 'dict'>
"""


# Dalam mengambil setiap nilai/elemen pada dictionary, Anda harus mengetahui key (kunci) untuk mengakses setiap value-nya (nilai). Hal ini berbeda dengan tipe data sebelumnya yang cukup mengharuskan Anda untuk menyebutkan indeksnya saja.
print(x[0])
print(x["name"])


# Menambah Data pada Dictionary
x["Job"] = "Web Developer"

print(x)

# Menghapus Data pada Dictionary
del x["isMarried"]

print(x)

# Mengubah Data pada Dictionary
x["name"] = "Dicoding"

print(x)
