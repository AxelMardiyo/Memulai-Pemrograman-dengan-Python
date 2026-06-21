# mengubah huruf besar/kecil
kata = 'dicoding'
kata = kata.upper()
print(kata)
kata = kata.lower()
print(kata)

# awalan & akhiran
print('Dicoding             '.rstrip() + " Indonesia") # menghapus whitespace di akhir/kanan
print('                 Dicoding'.lstrip()) # menghapus whitespace di awal/kiri
print("         Dicoding          ".strip()) # menghapus whitespace di kanan dan kiri

kata = 'CodeCodeDicodingCodeCode'
print(kata.strip("Code")) # menghapus karakter

print('Dicoding Indonesia'.startswith('Dicoding')) # mencari suatu kata pada awal string
print('Dicoding Indonesia'.endswith('Dicoding')) # mencari suatu kata pada akhir string

# memisah dan menggabung string
print(' '.join(['Dicoding','Indonesia', '!'])) # menggabung dengan spasi
print('123'.join(['Dicoding','Indonesia'])) # menggabung dengan karakter tertentu

print('Dicoding Indonesia !'.split()) # memisahkan dengan spasi/whitespace, outputnya list
print('''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n')) # memisahkan dengan enter, outputnya list

# mengganti elemen string (case sensitive)
string = "Ayo belajar Coding di Dicoding"
print(string.replace("Coding", "Pemrograman"))

# pengecekan string
kata = 'DICODING'
print(kata.isupper()) # cek uppercase/kapital
print(kata.islower()) # cek lowercase/kapitil

print(kata.isalpha()) # is alphabet?

kata = 'dicoding123'
print(kata.isalnum()) # is alfanumerik, hanya huruf atau hanya angka atau keduanya
print('123'.isdecimal()) # is desimal?, angka/numerik

print('         '.isspace()) # true jika isinya hanya whitespace(tab, spasi, newline, dll)
print('Dicoding Indonesia'.istitle()) # true jika berisi huruf kapital tiap awal kata

# formatting pada string
teks = 'c'
tambah_number = teks.zfill(5) # add 0 didepan string smpe jumlah total tertentu
print(tambah_number)

print('Dicoding'.rjust(20))  # jadi rata kanan
print('Dicoding'.rjust(20, '!')) # bisa jg selain whitespace
print('Dicoding'.ljust(20)) # rata kiri
print('Dicoding'.center(20, '-')) # teks jadi di tengah

# string literal petik
print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum\'at yang lalu.")
print(r'Dicoding\tIndonesia') # raw string, backslash tetap dibaca



