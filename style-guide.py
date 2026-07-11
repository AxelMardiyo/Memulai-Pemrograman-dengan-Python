# Perhatikan penggunaan spasi dari kedua kode berikut.
    
# Yes:
def munge(input: str):  # Menambahkan informasi parameter bertipe string
    pass
def munge() -> str:   # Menambahkan informasi return value bertipe string
    pass
    
# No:
def munge(input:str):  # Menambahkan informasi parameter bertipe string
    pass
def munge()->str:   # Menambahkan informasi return value bertipe string
    pass

# klo ada tipe data, di = pke spasi
def LuasPersegiPanjang(panjang: int = 2, lebar: int = None):
    pass

# Yes:
# klo gda tipe data, di = tnpa spasi
def LuasPersegiPanjang(panjang=2, lebar=None):
    luas = panjang*lebar
    return luas
 
# No:
def LuasPersegiPanjang(panjang = 2, lebar = None):
    luas = panjang*lebar
    return luas

# Yes:
def LuasPersegiPanjang(panjang:int = 2, lebar=None):
    pass
 
# No:
def LuasPersegiPanjang(panjang: int=2, lebar = None):
    pass


# Penamaan
'''
_diawali_sebuah_garis_bawah: penamaan ini dapat digunakan untuk penggunaan internal lemah yang merujuk pada penggunaannya dengan lingkup tertentu.
diakhiri_sebuah_garis bawah_: penamaan ini digunakan untuk mengatasi redundan dengan keyword/reserved words di Python.
__diawali_dua_garis bawah: menegaskan bahwa sebuah objek adalah bagian dari kelas tertentu.
__diawali_dan_diakhiri_dua_garis bawah__: Objek atau atribut tertentu yang diciptakan Python untuk digunakan dalam program. Contohnya adalah  __init__, __import__ or __file__.
'''



