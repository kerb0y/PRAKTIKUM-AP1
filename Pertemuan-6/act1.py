import persegi
import persegipanjang
import segitiga

def menu():
    print("\n=============== MENU ===============")
    print("1. Luas Persegi")
    print("2. Keliling Persegi")
    print("3. Luas Persegi Panjang")
    print("4. Keliling Persegi Panjang")
    print("5. Luas Segitiga")
    print("6. Keliling Segitiga")
    print("7. Keluar")
    
def main():
    menu()
    pilihan = int(input("\nMasukkan Pilihan Anda [1-7] = "))
    if pilihan == 1:
        sisi = float(input("\nMasukkan Sisi Persegi = "))
        print("Maka Luas Persegi Adalah ", persegi.luas(sisi))
    elif pilihan == 2:
        sisi = float(input("\nMasukkan Sisi Persegi = "))
        print("\nMaka Keliling Persegi Adalah ", persegi.keliling(sisi))
    elif pilihan == 3:
        p = float(input("\nMasukkan Panjang Persegi Panjang = "))
        l = float(input("\nMasukkan Lebar Persegi Panjang = "))
        print("\nMaka Luas Persegi Adalah ", persegipanjang.luas(p, l))
    elif pilihan == 4:
        p = float(input("\nMasukkan Panjang Persegi Panjang = "))
        l = float(input("\nMasukkan Lebar Persegi Panjang = "))
        print("\nMaka Keliling Persegi Adalah ", persegipanjang.keliling(p, l))
    elif pilihan == 5:
        a = float(input("\nMasukkan Alas Segitiga = "))
        t = float(input("\nMasukkan Tinggi Segitiga = "))
        print("\nMaka Luas Segitiga Adalah = ", segitiga.luas(a, t))
    elif pilihan == 6:
        sisi = float(input("\nMasukkan Sisi Segitiga = "))
        print("\nMaka Keliling Segitiga Adalah ", segitiga.keliling(sisi))
    else:
        print("\nPilihan Yang Anda Masukkan Tidak Valid")
        
main()
