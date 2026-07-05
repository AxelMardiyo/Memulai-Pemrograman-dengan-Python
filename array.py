# Pada array, nilai di dalamnya harus memiliki tipe data yang sama. Namun, pada list, nilai di dalamnya tidak harus memiliki tipe data yang sama. 

# Mendefinisikan array
var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr)

# Mendefinisikan isi array
# 1. Deklarasi sekaligus isi
var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 2. Mendefinisikan nilai default
var_arr = [0 for i in range(10)]
print(var_arr)

# Mengubah nilai default dengan nilai baru bedasarkan hasil suatu operasi
for i in range(10):
    var_arr[i] = i
print(var_arr)

# Mengakses Elemen Array
print(var_arr[0])

# Pemrosesan Sekuensial pada Arrayvar_arr = [1, 2, 3, 4, 5]

for i in range(len(var_arr)):
    current_element = var_arr[i]
    next_index = i+1
    
    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None
        
    print(f"Current element: {current_element}, next elements: {next_element}")

