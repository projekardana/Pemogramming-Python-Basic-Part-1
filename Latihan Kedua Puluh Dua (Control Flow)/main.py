list_cash_flow = [
2500000, 5000000, -1000000, -2500000, 5000000, 10000000,
-5000000, 7500000, 10000000, -1500000, 25000000, -2500000
]

total_pengeluaran, total_pemasukkan = 0, 0
for dana in list_cash_flow:
    if dana > 0:
        total_pemasukkan += dana
    else:
        total_pengeluaran += dana
    total_pengeluaran *= -1
    print(total_pengeluaran)
    print(total_pemasukkan)