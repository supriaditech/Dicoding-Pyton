x = 6
print(type(x))

x = 6.0
print(type(x))

x = 1 + 2j
print(type(x))

# Perlu diperhatikan bahwa tipe data numbers bersifat immutable yang artinya nilai di dalamnya tidak dapat diubah
var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))
