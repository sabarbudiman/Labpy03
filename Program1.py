print("\n Mencari total keuntungan selama 8 bulan\n")

Modal = 100000000
Hasil = 0
Bulan = 0

Hitung = [int(0), int(0), int(Modal) *.1 , int(Modal) *.1, int(Modal) *.5, int(Modal)* .5, int(Modal) *.5, int(Modal) *.2]
print("Modal awal seorang pengusaha : ", Modal )
for i in Hitung :
    Hasil = Hasil + i
    Bulan += 1
    print('Laba bulen ke : ',Bulan,'Sebesar : ', i)

print("\nTotal laba yang di dapat adalah: ", Hasil)