import os
import random
os.system('cls' if os.name == 'nt' else 'clear')

# mengecek pointer pada list
print("\n============ Mengecek Pointer Pada List ============")
print("Before value is updated: ")
listAngka = [1, 2, 3]; listAngkaKedua = listAngka
print('List Angka Pertama =', listAngka, '|| id =', id(listAngka))
print('List Angka Kedua =', listAngkaKedua, '|| id =', id(listAngkaKedua))

print("\nAfter value is updated: ")
listAngka = [1, 2, 3]; listAngkaKedua = [3, 2, 1]
print('List Angka Pertama =', listAngka, '|| id =', id(listAngka))
print('List Angka Kedua =', listAngkaKedua, '|| id =', id(listAngkaKedua))
print("====================================================\n")

os.system('pause')

# mengecek pointer pada tuple
print("\n============ Mengecek Pointer Pada Tuple ============")
print("Before value is updated: ")
tupleAngka = (1, 2, 3); tupleAngkaKedua = tupleAngka
print('List Angka Pertama =', tupleAngka, '|| id =', id(tupleAngka))
print('List Angka Kedua =', tupleAngkaKedua, '|| id =', id(tupleAngkaKedua))

print("\nAfter value is updated: ")
tupleAngka = (1, 2, 3); tupleAngkaKedua = (3, 2, 1)
print('List Angka Pertama =', tupleAngka, '|| id =', id(tupleAngka))
print('List Angka Kedua =', tupleAngkaKedua, '|| id =', id(tupleAngkaKedua))
print("====================================================\n")

os.system('pause')

# mengecek pointer pada set
print("\n============ Mengecek Pointer Pada Set ============")
print("Before value is updated: ")
setAngka = {1, 2, 3}; setAngkaKedua = setAngka
print('List Angka Pertama =', setAngka, '|| id =', id(setAngka))
print('List Angka Kedua =', setAngkaKedua, '|| id =', id(setAngkaKedua))

print("\nAfter value is updated: ")
setAngka = {1, 2, 3}; setAngkaKedua = {3, 2, 1}
print('List Angka Pertama =', setAngka, '|| id =', id(setAngka))
print('List Angka Kedua =', setAngkaKedua, '|| id =', id(setAngkaKedua))
print("====================================================\n")