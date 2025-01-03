# Konversi Integer ke Float
print(float(5))
# Konversi Float ke Integer
print(int(5.6))
print(int(-5.6))

# Konversi dari-dan-ke String
print(int("25"))
print(str(25))
print(float("25"))
print(str(25.6))

# Perlu Anda perhatikan bahwa konversi dari-dan-ke string akan melalui pengujian dan dipastikan validitasnya. Jika pengujian dan validitasnya gagal, error akan dihasilkan.
print(int("1p"))

# Konversi Kumpulan Data
print(set([1, 2, 3]))
print(tuple({5, 6, 7}))
print(list("hello"))

# Konversi ke Dictionary
print(dict([[1, 2], [3, 4]]))

# Konversi list dari beberapa tuple yang isinya pasangan nilai menjadi dictionary.
print(dict([(3, 26), (4, 44)]))
