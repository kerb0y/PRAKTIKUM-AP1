# tipe100.py
from rumus import Persegi, PersegiPanjang, Segitiga

def menu():
    # Menampilkan menu pilihan
    print("\n=============== MENU ===============")
    print("1. Luas Persegi")
    print("2. Keliling Persegi")
    print("3. Luas Persegi Panjang")
    print("4. Keliling Persegi Panjang")
    print("5. Luas Segitiga")
    print("6. Keliling Segitiga")
    print("7. Keluar")
    
def main():
    # Memanggil fungsi menu
    menu()
    
    # Input pilihan pengguna
    pilihan = int(input("\nMasukkan Pilihan Anda [1-7] = "))
    
    # Membuat instance dari kelas Persegi, PersegiPanjang, dan Segitiga
    persegi = Persegi()
    persegi_panjang = PersegiPanjang()
    segitiga = Segitiga()
    
    if pilihan == 1:
        # Menghitung dan menampilkan luas Persegi
        sisi = float(input("\nMasukkan Sisi Persegi = "))
        print("Maka Luas Persegi Adalah ", persegi.luas(sisi))
    elif pilihan == 2:
        # Menghitung dan menampilkan keliling Persegi
        sisi = float(input("\nMasukkan Sisi Persegi = "))
        print("\nMaka Keliling Persegi Adalah ", persegi.keliling(sisi))
    elif pilihan == 3:
        # Menghitung dan menampilkan luas Persegi Panjang
        p = float(input("\nMasukkan Panjang Persegi Panjang = "))
        l = float(input("\nMasukkan Lebar Persegi Panjang = "))
        print("\nMaka Luas Persegi Panjang Adalah ", persegi_panjang.luas(p, l))
    elif pilihan == 4:
        # Menghitung dan menampilkan keliling Persegi Panjang
        p = float(input("\nMasukkan Panjang Persegi Panjang = "))
        l = float(input("\nMasukkan Lebar Persegi Panjang = "))
        print("\nMaka Keliling Persegi Panjang Adalah ", persegi_panjang.keliling(p, l))
    elif pilihan == 5:
        # Menghitung dan menampilkan luas Segitiga
        a = float(input("\nMasukkan Alas Segitiga = "))
        t = float(input("\nMasukkan Tinggi Segitiga = "))
        print("\nMaka Luas Segitiga Adalah = ", segitiga.luas(a, t))
    elif pilihan == 6:
        # Menghitung dan menampilkan keliling Segitiga
        sisi = float(input("\nMasukkan Sisi Segitiga = "))
        print("\nMaka Keliling Segitiga Adalah ", segitiga.keliling(sisi))
    else:
        # Menampilkan pesan jika pilihan tidak valid
        print("\nPilihan Yang Anda Masukkan Tidak Valid")
        
# Memanggil fungsi main
main()
