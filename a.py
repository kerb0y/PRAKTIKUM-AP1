import psg
import pp
import s

def menu():
    print("========== MENU ==========")
    print("1. Luas Persegi")
    print("2. Keliling Persegi")
    print("3. Luas Persegi Panjang")
    print("4. Keliling Persegi Panjang")
    print("5. Luas Segitiga")
    print("6. Keliling Segitiga")
    print("7. Keluar")

def main():
    menu()
    pilihan = int(input("\nMasukkan Pilihan Anda [1-7] : "))
    if pilihan == 1:
        sisi = float(input("\nMasukkan sisi persegi : "))
        print("\nMaka luas persegi adalah ", psg.luas(sisi))
    elif pilihan == 2:
        sisi = float(input("\nMasukkan sisi persegi : "))
        print("\nMaka keliling persegi adalah ", psg.keliling(sisi))
    elif pilihan == 3:
        p = float(input("\nMasukkan panjang persegi panjang : "))
        l = float(input("\nMasukkan lebar persegi panjang : "))
        print("\nMaka luas persegi panjang adalah ", pp.luas(p, l))
    elif pilihan == 4:
        p = float(input("\nMasukkan panjang persegi pajang: "))
        l = float(input("\nMasukkan lebar persegi pajang: "))
        print("\nMaka luas persegi adalah ", pp.keliling(p, l))
    elif pilihan == 5:
        a = float(input("\nMasukkan alas segitiga : "))
        t = float(input("\nMasukkan tinggi segitiga : "))
        print("\nMaka luas segitiga adalah ", s.luas(a, t))
    elif pilihan == 6:
        sisi = float(input("\nMasukkan sisi segitiga : "))
        print("\nMaka keliling segitiga adalah ", s.keliling(sisi))
    else:
        print("\nPilihan yang anda masukkan tidak valid")
main()