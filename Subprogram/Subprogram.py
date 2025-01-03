# Luas pertama
panjang = 5
lebar = 10

# Rumus perhitungan luas persegipanjang adalah panjang dikali lebar
luas_persegi_panjang = panjang * lebar
print(luas_persegi_panjang)

# Luas kedua
panjang = 4
lebar = 15

# Rumus perhitungan luas persegipanjang adalah panjang dikali lebar
luas_persegi_panjang = panjang * lebar
print(luas_persegi_panjang)


def mencari_luas_persegi_panjang(panjang, lebar):
    """
    Fungsi mencari_luas_persegi_panjang digunakan untuk menghitung luas persegipanjang
    dengan panjang dan lebar yang diberikan.

    Struktur fungsi ini terdiri dari:
    - parameter panjang dan lebar yang diberikan untuk menghitung luas
    - variabel luas_persegi_panjang untuk menyimpan hasil perhitungan
    - return statement untuk mengembalikan nilai hasil perhitungan

    Parameters
    ----------
    panjang : int
        Panjang persegipanjang
    lebar : int
        Lebar persegipanjang

    Returns
    -------
    int
        Luas persegipanjang
    """
    luas_persegi_panjang = panjang * lebar
    return luas_persegi_panjang


persegi_panjang_pertama = mencari_luas_persegi_panjang(5, 10)
print(persegi_panjang_pertama)

persegi_panjang_kedua = mencari_luas_persegi_panjang(4, 15)
print(persegi_panjang_kedua)
