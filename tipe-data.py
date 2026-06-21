# Variabel name
"""aefhishf
sefs
fbues"""

# formatted string
name = "Axel Pratama"
print(f"Hello, nama saya {name}")

# %-formatting
name = "Axel Pratama"
print("Hello, nama saya %s" % (name))

# str.format()
name = "Axel Pratama"
print("Hello, nama saya {}".format(name))


# list (kyk array tpi tipe datanya bisa beda-beda)
list = [1, 2.2, "Dicoding"]
list[0] = "Indonesia"
print(list)

# tuple (sprti array, tpi tidak dapat diubah)
variabel_tuple = (1, "Dicoding", True)
print(variabel_tuple)

# set (duplikat diabaikan), = himpunan
variabel_set = {1, 2, 5, 7, 2}
print(variabel_set)

set1 = {1, 2, 3, 5}
set2 = {1, 4, 6, 7}

union = set1.union(set2) # gabungan
intersection = set1.intersection(set2) # irisan

print(union)
print(intersection)

# dictionary (kayak object)
dictionary1 = {
    'name': 'Axel Pratama',
    'age': 20,
    'isMarried': False
}

dictionary1['Job'] = 'Web Developer' # add data
del dictionary1['isMarried'] # delete data
dictionary1['name'] = 'Axel Mardiyo' # update data

print(dictionary1)

