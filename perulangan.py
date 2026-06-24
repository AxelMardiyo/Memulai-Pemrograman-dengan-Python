# For
var_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in var_list:
    print(i)

for i in range(10):
    print(
        i
    )  # tampilnya 0-9, karena pada dasarnya "range()" menghasilkan urutan dimulai dari index 0

# range(start, stop, step)
for i in range(1, 10, 2):
    print(i)  # akan menampilkan angka ganjil dari 1 - 9


# While
counter = 1
while counter <= 5:
    print(counter)
    counter += 1


# Nested For
for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)


# Kontrol Perulangan
# Break
for i in range(2):  # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 1:
            break  # Menghentikan perulangan dalam jika j = 1

for huruf in "Dico ding":
    if huruf == " ":
        break
    print("Huruf saat ini: {}".format(huruf))  # berhenti smpe spasi aja

# Continue
for huruf in "Dico ding":
    if huruf == " ":
        continue
    print("Huruf saat ini: {}".format(huruf))  # spasi nya di skip


# Else setelah For
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 6:
        print("Angka ditemukan! Program berhenti!")
        break
else:
    print(
        "Angka tidak ditemukan."
    )  # ketika for tidak ada yg sesuai, maka else akan dijalankan

# Else setelah While
count = 0

while count < 3:
    print("Dicoding Indonesia")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")

n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print(
        "Loop selesai"
    )  # loop berhenti krna break, dan else tidak dijalankan krna while berhenti saat msih true


# Pass, menginginkan sebuah pernyataan atau blok pernyataan (statement), tetapi tidak ada tindakan atau program tidak melakukan apa pun.
x = 10
if x > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")


# List Comprehension, membuat list baru dari yang sudah ada pake perulangan
angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
    pangkat.append(n**2)
print(pangkat)

# versi singkat
angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)
