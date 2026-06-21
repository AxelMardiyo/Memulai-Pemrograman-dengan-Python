#  Panjang
contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]

print(contoh_list)
print(len(contoh_list)) # menghitung banyaknya elemen

contoh_list = set([1, 3, 3, 5, 5, 5, 7, 7, 9])

print(contoh_list)
print(len(contoh_list))

contoh_list = "Belajar Python"

print(contoh_list)
print(len(contoh_list)) # pada string akan dihitung jumlah karakter

# min max
angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka)) # nilai max
print(max(angka)) # nilai min

# mencari berapa kali suatu objek muncul dalam list
genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(6))

string = "Belajar Python di Dicoding sangat menyenangkan"
substring = "a"
print(string.count(substring)) # menghitung banyaknya substring/huruf "a"

# mengetahui nilai/objek dalam list
kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)

# mengisi variabel dari list/tuple
data = ['shirt', 'white', 'L']
apparel, color, size = data

print(data)
print(apparel)
print(color)
print(size)

# sort
kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort() # kalo string diurutkan dari huruf depan, berdasarkan urutan ASCII
print(kendaraan)

kendaraan.sort(reverse=True) # reverse sort, sort tidak bs dipake di list yang isinya angka dan string sekaligus
print(kendaraan)



