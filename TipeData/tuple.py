x = (1, "Dicoding", 1 + 3j)
print(type(x))

# indexing dan slicing pada tuple
y = (5, "program", 1 + 3j)
print(y[1])
print(y[0:3])

# Tuple bersifat immutable yang artinya tidak dapat diubah.
x = (5, "program", 1 + 3j)
x[1] = "Dicoding"
