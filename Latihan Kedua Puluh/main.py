list_tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]

#For Loops with break
print("For Loops With Break")
total_tagihan_break = 0
for tagihan in list_tagihan:
    if tagihan < 0:
        print("Terdapat angka minus dalam tagihan, Perulangan di hentikan!")
        break
    total_tagihan_break += tagihan
    print("Total tagihan %d." % total_tagihan_break)
    print()

#For Loops With Continue
print("For Loops with Continue")
total_tagihan_continue = 0
for tagihan in list_tagihan:
    if tagihan < 0:
        print("Terdapat angka minus dalam tagihan, tagihan %d dilewati!" % tagihan)
        continue
    total_tagihan_continue += tagihan
    print("Total tagihan %d." % total_tagihan_continue)
    print()

