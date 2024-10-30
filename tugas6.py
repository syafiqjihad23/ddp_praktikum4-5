kendaraan = ["Toyota Celica 2.0 GT-i", "Mobil Sport", 1998, "Hijau Tua", 4]
print("Kendaraan Saya")
print(kendaraan)
print("-------")

kendaraan.extend([600000000, "Manual"])
print(kendaraan)
print("-------")

kendaraan.insert(2, "Toyota")
print(kendaraan)
print("-------")

print("Ini adalah program sederhana untuk menghitung luas bangun datar")
print(f"Pilih Menu angka 1-3: \n1: Persegi\n2: Lingkaran\n3: Segitiga ")
pilihMenu = int(input("Silakan pilih menu dengan mengetik angka 1-3: "))
print(pilihMenu)

match pilihMenu:
    case 1:
        print("Ini adalah menu untuk menghitung luas persegi")
        sisi = int(input("Silahkan masukan nilai yang mau dihitung: "))
        hitung = sisi * sisi
        print(f"Luas persegi adalah: {hitung}")
    case 2:
        print("Ini adalah menu untuk menghitung luas lingkaran")
        r= int(input("Silakan masukan nilai yang mau dihitung: "))
        Pi = 3.14
        hitung = Pi * r * r
        print(f"Luas lingkaran adalah: {hitung}")
    case 3:
        print("Ini adalah menu untuk menghitung luas segitiga")
        angka = int(input("Silakan masukan nilai yang mau dihitung: "))
        hitung = (1/2) * angka * angka
        print(f"Luas segitiga adalah: {hitung}")
        
    case _:
        print("Pilihan tidak valid, silahkan pilih antara 1-3")
    