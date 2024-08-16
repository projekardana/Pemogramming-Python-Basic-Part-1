'''
Latihan Nilai Prioritas Operator dalam Python Part 2

'''
nilai = (1 - 0.3) * 100
# Nilai = 0.7 * 100
# Nilai = 70

print(nilai) #Menghasilkan Nilai 70

nilai = (3 + 2) ** 2 + (4+4) / 2% 4
# berikut merupakan simulasi dari urutan pengerjaan yang dilakukan python,
# 1. Python akan mengerjakan bagian di dalam kurung
#paling kiri
#nilai 5 ** 2 + (4+4) / 2 % 4
# 2. Python akan mengerjakan bagian di dalam kurung
# yang tersisa 
# nilai 5 ** 2 + 8 / 2 % 4
# 3. Operator Pangkat akan dikerjakan oleh Python
# nilai 25 + 8 / 2 % 4
# 4. Operator akan menjalankan operator pembagian dikarenakan prioritasnya 
#lebih tinggi di bandingkan operator penambahan
# nilai 25 + 4 % 4
# 5. Python akan mengerjakan operator modulus dikarenakan prioritasnya
# Lebih tinggi dibandingkan operator penambahan
# nilai 25 + 0
# 6. Operator akan mengerjakan operator penambahan
# nilai = 25
print(nilai) # akan menghasilkan 25.0
