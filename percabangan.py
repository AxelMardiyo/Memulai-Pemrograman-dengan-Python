keterseidaan = "Daging ayam"

if keterseidaan == "Daging ayam":
    print("Ibu membeli dan memasak ayam")
else:
    print("Ibu membeli dan memasak tempe")

score = 100

if score == 100:
    print("Skor anda sempurna")

# nilai kosong / null dianggap False, sebalinya True
x = ""

if x:
    print("Ini True")

# One-liner if statement
if score == 100:
    print("Nilai Anda sempurna!")

# else
tinggi_badan = 120

if tinggi_badan >= 160:
    print("Anda boleh menaiki roller coaster")
else:
    print("Anda tidak diperbolehkan menaiki roller coaster")

# elif, else if
nilai = 65

if nilai >= 80:
    print("Selamat! Anda mendapat nilai A")
    print("Pertahankan!")
elif nilai >= 70:
    print("Hore! Anda mendapat nilai B")
    print("Tingkatkan!")
elif nilai >= 60:
    print("Hmm.. Anda mendapat nilai C")
    print("Ayo semangat!")
else:
    print("Waduh, Anda mendapat nilai D")
    print("Yuk belajar lebih giat lagi!")


# menambahkan AND atau OR
nilai = 81
perilaku = "tidak baik"

if nilai >= 80 and perilaku == "baik":
    print("Selamat! Anda mendapat nilai A dan telah berkelakuan baik")
    print("Pertahankan!")
elif nilai >= 80 and perilaku != "baik":
    print("Kamu mendapatkan nilai A, tetapi perilaku Anda kurang baik")
    print("Perbaiki lagi ya!")
else:
    print("Yuk belajar lebih giat lagi!")

# ternary operator
lulus = True
print("selamat") if lulus else print("perbaiki")

# sama dengan dibawah ini
if lulus:
    print("Selamat") 
else:
    print("Perbaiki")
    
# ternary tuples, 
kelulusan = ("Perbaiki, Anda belum lulus.","Selamat, Anda lulus!")[lulus]
