# Praktek Tugas Operators 

sepatu = {'nama':'Sepatu Niko', 'harga':150000, 'diskon':30000}
Baju = {'nama':'Baju Unikloh', 'harga':80000, 'diskon':8000}
celana = {'nama':'Celana Lepis', 'harga':200000, 'diskon':60000}

harga_sepatu = sepatu['harga'] - sepatu['diskon']
harga_baju = Baju['harga'] - Baju['diskon']
harga_celana = celana['harga'] - celana['diskon']

total_harga = (harga_sepatu + harga_baju + harga_celana) * 1.1
print(total_harga)