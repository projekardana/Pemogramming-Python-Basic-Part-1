## Tugas Praktek 3
sepatu = {'nama':'niko', 'harga':150000, 'diskon':30000}
baju = {'nama':'Unikloh', 'harga':80000, 'diskon':8000}
celana = {'nama':'Lepis', 'harga':200000, 'diskon':60000}

##Tugas Praktek 4
sepatu = {'nama':'niko', 'harga':'150000', 'diskon':30000}
baju = {'nama':'Unikloh', 'harga':'80000', 'diskon':8000}
celana = {'nama':'Lepis', 'harga':'200000', 'diskon':60000}
daftar_belanja = [sepatu, baju, celana]

##Tugas Praktek 5
#Data Yang dinyatakan ke dalam Dictionary
sepatu = {'nama':'Sepatu niko', 'harga':150000, 'diskon':30000}
baju = {'nama':'Baju Unikloh', 'harga':80000, 'diskon':8000}
celana = {'nama':'Celana Lepis', 'harga':200000, 'diskon':60000}
#Hitunglah Harga masing-masing data setelah di kurangi diskon
harga_sepatu = sepatu['harga'] - sepatu['diskon']
harga_baju = baju['harga'] - baju['diskon']
harga_celana = celana['harga'] - celana['diskon']
#Hitung Harga Total
total_harga = harga_sepatu + harga_baju + harga_celana
#Hitung Harga Kenak Pajak
total_pajak = total_harga * 0.1
#Cetak Total Harga + total_pajak
print(total_harga + total_pajak)