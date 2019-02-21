print('Menampilkan Bilangan acak yang lebih kecil dari 0.5\n')

import random

N = int(input("Masukkan Nilai N: "))
A = 0
for i in range(N):
    A += 1
    N = random.uniform(0.0,0.5)
    print('Data ke : ',A, '==>',N)

print("Selesai")
