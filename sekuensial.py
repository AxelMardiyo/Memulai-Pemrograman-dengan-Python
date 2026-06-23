# Sekuensial: Program dijalankan secara berurutan dari atas ke bawah
print("Selamat datang dalam program Python!\n")
print("Silakan masukkan data diri Anda.")
nama = input("Masukkan nama Anda: ")
tahun_lahir = input("Masukkan tahun lahir Anda: ")
umur = 2023 - int(tahun_lahir)
 
print(f"Selamat datang {nama} dalam program Python, per 2023 umur Anda adalah {umur} tahun.\n")
print("Terima kasih telah menggunakan program Python!")

# Python Interpreter
for i in range(10):
    print(i) # aman karena masih 1 blok, menggunakan indentasi (tab)

# for i in range(10):
# print(i) #error, karena beda blok

# Case Sensitive
teks = "Dicoding"
Teks = "Indonesia"

print(teks)
print(Teks)

# One-liner
# before one-liner
x = 1
y = 2

temp = x
x = y
y = temp

print("Setelah pertukaran: ")
print("x = ", x)
print("y =",  y)

# after one-liner
x = 1
y = 2

x, y = y, x    # One-liner

print('Setelah pertukaran: ')
print('x =', x)
print('y =', y)