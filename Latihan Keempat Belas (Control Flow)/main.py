### Python Conditioning For Decision Part 2

#Statement if
x = 4
if x % 2 == 0: # Jika sisa bagi x dengan 2 sama dengan 0
    print("x habis dibagi dengan 2")
#Statement if.... elif...else
x = 7
if x % 2 == 0: #Jika sisa bagi x dengan 2 sama dengan 0
    print("x habis dibagi dengan 2")
elif x % 3 == 0: #Jika sisa bagi x dengan 3 sama dengan 0
    print("x habis dibagi dengan 3")
elif x % 5 == 0: #Jika sisa bagi x dengan 5 sama dengan 0
    print("x hasil dibagi dengan 5")
else:
    print("Tidak ada Hasil dibagi dua, tiga ataupun lima")