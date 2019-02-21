print("Menentukan Bilangan terbesar\n")

A = 0
while True:
    B = int(input("Masukkan Bilangan : "))
    if A < B:
        A = B
    if B == 0:
        break
print("\nBilangan terbesarnya adalah : ", A)