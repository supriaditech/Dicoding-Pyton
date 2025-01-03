x = {1, 2, 7, 2, 3, 13, 3}
print(x[0])

# Set juga bersifat unik, artinya, data yang Anda simpan pada set tidak akan ada duplikat
y = {1, 2, 7, 2, 3, 13, 3}
print(y)
print(type(y))

# Terakhir, set adalah himpunan dalam matematika. Ini maknanya Anda dapat melakukan operasi union (gabungan) dan intersection (irisan) pada set. Python menyediakan method “.union()” dan “.intersection()” untuk tipe data set.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
print("Union:", union)

intersection = set1.intersection(set2)
print("Intersection:", intersection)
