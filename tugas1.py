bilangan= int(input("Masukan angka\n= "))

hasil= bilangan % 2
if hasil == 0 :
    print(f"Angka {bilangan} sama dengan angka genap")
elif hasil ==1:
    print(f"Angka {bilangan} sama dengan angka ganjil")
else :
    print(f"Angka gak jelas")
