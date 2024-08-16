tagihan_ke = "Mr. Yoyo"
warehousing = {"Harga_Harian":1000000, "Total_Hari":15}
cleansing = {"Harga_Harian":1500000, "Total_Hari":10}
integration = {"Harga_Harian":2000000, "Total_Hari":15}
transform = {"Harga_Harian":2500000, "Total_Hari":10}

sub_warehousing = warehousing["Harga_Harian"] * warehousing["Total_Hari"]
sub_cleansing = cleansing["Harga_Harian"] * cleansing["Total_Hari"]
sub_integration = integration["Harga_Harian"] * integration["Total_Hari"]
sub_transform = transform["Harga_Harian"] * transform["Total_Hari"]
total_harga = (sub_warehousing + sub_cleansing + sub_integration + sub_transform)
print("Tagihan Kepada :")
print(tagihan_ke)
print("Selamat Anda Harus Membayar Tagihan Anda Sebesar :")
print(total_harga)

##Tugas Praktek 2

jam = 17
tagihan_ke = "Mr. Yoyo"
warehousing = {"Harga_Harian":1000000, "Total_Hari":15}
cleansing = {"Harga_Harian":1500000, "Total_Hari":10}
integration = {"Harga_Harian":2000000, "Total_Hari":15}
transform = {"Harga_Harian":2500000, "Total_Hari":10}

sub_warehousing = warehousing["Harga_Harian"] * warehousing["Total_Hari"]
sub_cleansing = cleansing["Harga_Harian"] * cleansing["Total_Hari"]
sub_integration = integration["Harga_Harian"] * integration["Total_Hari"]
sub_transform = transform["Harga_Harian"] * transform["Total_Hari"]
total_harga = (sub_warehousing + sub_cleansing + sub_integration + sub_transform)
print("Tagihan Kepada :")
print(tagihan_ke)
print("Selamat Anda Harus Membayar Tagihan Anda Sebesar :")
print(total_harga)

if jam > 19:
    print("Selamat Malam Anda Harus Membayar Tagihan Sebesar :")
elif jam < 17:
    print("Selamat Sore Anda Harus Membayar Tagihan Sebesar :")
elif jam > 12:
    print("Selamat Siang Anda harus Membayar Tagihan Sebesar : ")
else:
    print("Selamat Pagi Anda Harus Membayar Tagihan Sebesar :")
print(total_harga)