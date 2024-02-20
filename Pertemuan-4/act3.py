def menu():
    print("===============================================================")    
    print("                         ACTIVITY 3                            ")
    print("===============================================================")
    print("1. Segitiga Bintang")
    print("2. Grade Nilai")
    print("3. Keluar")
    
def segitiga():
    print("\n--------------------- SEGITIGA BINTANG ----------------------")
    tinggi = int(input("Masukkan tinggi segitiga: "))
    for i in range (1, tinggi + 1):
        print(" " * (tinggi - i) + "*" * (2 * i - 1))
    menu()
    
def grade():
    rata = int(input("\nMasukkan nilai rata-rata anda : "))
    
    if rata >= 88:
        print("Selamat Kamu Mendapatkan Grade A")
    elif rata >= 80:
        print("Selamat Kamu Mendapatkan Grade B")
    elif rata >= 74:
        print("Selamat Kamu Mendapatkan Grade C")
    else:
        print("Kamu Mendapatkan Grade D")
    menu()
    
menu()

def keluar():
    exit(0)
    
while menu:
    print()
    pilih = int(input("Masukkan Pilihan Anda [1-3] : "))
    
    if pilih == 1:
        segitiga()
    elif pilih == 2:
        grade()
    else:
        keluar()