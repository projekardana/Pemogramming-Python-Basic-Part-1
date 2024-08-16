#While Loops Part 2

tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
i = 0
jumlah_tagihan = len(tagihan)
total_tagihan = 0
while i < jumlah_tagihan:
      # jika terdapat tagihan ke-i yang bernilai minus (di bawah nol),
      # pengulangan akan dihentikan
      if tagihan[i] < 0:
            total_tagihan = -1
            print("Terdapat angka minus di dalam tagihan, perhitungan di hentikan")
            break
            total_tagihan += tagihan[i]
            i += 1
            print(total_tagihan)