status = input(("""Silahkan pilih status keanggotaan seperti di bawah ini
GOLD | SILVER | BRONZE masukan pilihan anda = """))

if status.upper() == "GOLD" or status.upper() == "SILVER":
    print("Selamat anda mendapatkan diskon!")
else :
    print("Mohon maaf kamu tidak mendapatkan diskon")