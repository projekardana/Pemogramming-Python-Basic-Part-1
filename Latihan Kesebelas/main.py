''''
Nilai Prioritas Operator dalam Python Part 1
'''
#kode awal
total_harga = 150000
potongan_harga = 0.3
pajak = 0.1 # Pajak dalam persen ~ 10%
harga_bayar = 1 - potongan_harga # baris pertama
harga_bayar *= total_harga # baris kedua
pajak_bayar = pajak * harga_bayar #baris ketiga
harga_bayar += pajak_bayar #baris keempat
print("Kode Awal - harga_bayar : ", harga_bayar)
#Penyederhanaan Baris Kode dengan menerapkan proritas operator
total_harga = 150000
potongan_harga = 0.3
pajak = 0.1 #pajak dalam persen ~ 10%
harga_bayar = (1 - potongan_harga) * total_harga #baris pertama
harga_bayar += harga_bayar * pajak #baris kedua
print("Penyederhanaan kode - harga_bayar = ", harga_bayar)