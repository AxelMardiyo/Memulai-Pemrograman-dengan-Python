# Deklarasi fungsi
def mencari_luas_persegi_panjang(panjang,lebar):
    
    # docstring, dokumentasi untuk sebuah funsi
    """
    Fungsi ini digunakan untuk menghitung luas persegi panjang.

    Args:
        panjang (int): Panjang persegi panjang.
        lebar (int): Lebar persegi panjang.

    Returns:
        int: Luas persegi panjang hasil perhitungan.
    """
    
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

# Memanggil fungsi
mencari_luas_persegi_panjang(10,5)
print(mencari_luas_persegi_panjang)

# Var-Positional (Variadic Positional Parameter) menampung jumlah argumen posisi yang bervariasi
def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(1, 2, 3))

# Var-Keyword (Variadic Keyword Parameter) menampung jumlah keyword argument yang bervariasi
def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info

print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))

# Fungsi Anonim (Lambda Expression)
mencari_luas_persegi_panjang = lambda panjang, lebar: panjang*lebar
print(mencari_luas_persegi_panjang(5,10))

