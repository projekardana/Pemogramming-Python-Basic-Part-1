# Python Primitive Loop Control
"""Loop Control merupakan salah satu fitur yang mengizinkan penggunanya untuk melakukan serangkaian aksi, selama suatu kondisi yang telah ditetapkan bernilai benar. Dalam Python, terdapat dua bentuk primitif dari loop kontrol (struktur pengulangan), yaitu

while loops
for loops

"""
###Contoh : 
#Tagihan
tagihan = [50000, 75000, 125000, 300000, 200000]
#Tanpa Menggunakan While Loop
total_tagihan = tagihan[0] + tagihan[1] + tagihan[2] + tagihan[3] + tagihan[4]
print(total_tagihan)
#Dengan Menggunakan While Loop
i = 0 #Sebuah Variabel untuk mengakses elemen satu per satu
jumlah_tagihan = len(tagihan) #Panjang (Jumlah elemen list dalam) list tagihan
total_tagihan = 0 #Mula Mula set tagihan ke 0
while i < jumlah_tagihan: # selama nilai i kurang dari jumlah_tagihan
    total_tagihan += tagihan[i] # tambahkan tagihan[i] ke total_tagihan
    i += 1  # tambahkan nilai i dengan 1 untuk memproses tagihan selanjutnya.
print(total_tagihan)


