x = "Dicoding"
print(type(x))

# menggunakan tiga single quote atau double quote untuk menyimpan string yang lebih dari satu baris (multi-line).

multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu."""

print(multi_line)

# String merupakan urutan karakter yang setiap karakternya memiliki indeks.
x = "Dicoding"
print(x[0])


# Namun, Anda tidak dapat mengubah substring di dalamnya. Ini dikarenakan string pada Python bersifat immutable.

x = "Dicoding"
x[0] = "F"

# mengakses beberapa substring dengan menggunakan metode indexing dan slicing.
x = "Dicoding"
print(x[2:])

# Formatted String\
name = "Supriadi"
print(f"Hello, nama saya {name}")

# %-formatting
name = "Supriadi"
print("Nama saya %s" % (name))

# str.format()
name = "Supriadi"
print("Nama saya {}".format(name))
