x = [1, 2.2, "Dicoding"]
print(type(x))

y = [1, "Dicoding", True, 1.0]

print(y[2])

# List Python bersifat mutable yang artinya nilai di dalamnya dapat diubah.
a = [1, 2.2, "Dicoding"]
a[0] = "Indonesia"
print(a)

# Konsep indexing merujuk kepada pengambilan data dalam Python berdasarkan indeksnya. Beberapa cara untuk melakukan indexing sebagai berikut.

b = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(b[0])
print(b[2])
print(b[-1])
print(b[-3])

# implementasi slicing pada Python.
c = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(c[0:5:2])
print(c[1:])
print(c[:3])
