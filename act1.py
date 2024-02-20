import persegi # mengimpor module persegi dari file persegi.py
import persegipanjang # mengimpor module persegi dari file persegipanjang.py
import segitiga # mengimpor module persegi dari file module.py

# membuat fungsi menu & menampilkan judul dan isi menu
def menu():
    print("\n=============== MENU ===============")
    print("1. Luas Persegi")
    print("2. Keliling Persegi")
    print("3. Luas Persegi Panjang")
    print("4. Keliling Persegi Panjang")
    print("5. Luas Segitiga")
    print("6. Keliling Segitiga")
    print("7. Keluar")
    
# membuat fungsi main 
def main():
    # memanggil fungsi menu
    menu()
    
    # variabel pilhan diisi dalam bentuk integer 1-7
    pilihan = int(input("\nMasukkan Pilihan Anda [1-7] = "))
    
    # jika pilihan = 1 
    if pilihan == 1:
        # input sisi menggunakan float untuk bilangan pecahan 
        sisi = float(input("\nMasukkan Sisi Persegi = "))
        # print hasil luas persegi dengan memanggil module persegi dengan fungsi def luas dan data nilai variabel sisi
        print("Maka Luas Persegi Adalah ", persegi.luas(sisi))
    # jika pilhan = 2
    elif pilihan == 2:
        # input sisi menggunakan float untuk bilangan pecahan
        sisi = float(input("\nMasukkan Sisi Persegi = "))
        # print hasil keliling persegi dengan memanggil module persegi dengan fungsi def keliling dan data nilai variabel sisi
        print("\nMaka Keliling Persegi Adalah ", persegi.keliling(sisi))
    # jika pilhan = 3
    elif pilihan == 3:
        # input p menggunakan float untuk bilangan pecahan
        p = float(input("\nMasukkan Panjang Persegi Panjang = "))
        # input l menggunakan float untuk bilangan pecahan
        l = float(input("\nMasukkan Lebar Persegi Panjang = "))
        # print hasil luas persegi dengan memanggil module persegipjg dengan fungsi def luas dan data nilai variabel sisi
        print("\nMaka Luas Persegi Adalah ", persegipanjang.luas(p, l))
    # jika pilhan = 4
    elif pilihan == 4:
        p = float(input("\nMasukkan Panjang Persegi Panjang = "))
        l = float(input("\nMasukkan Lebar Persegi Panjang = "))
        print("\nMaka Keliling Persegi Adalah ", persegipanjang.keliling(p, l))
    # jika pilhan = 5
    elif pilihan == 5:
        a = float(input("\nMasukkan Alas Segitiga = "))
        t = float(input("\nMasukkan Tinggi Segitiga = "))
        print("\nMaka Luas Segitiga Adalah = ", segitiga.luas(a, t))
    # jika pilhan = 6
    elif pilihan == 6:
        sisi = float(input("\nMasukkan Sisi Segitiga = "))
        print("\nMaka Keliling Segitiga Adalah ", segitiga.keliling(sisi))
    # jika pilihan tidak diantara 1-6
    else:
        print("\nPilihan Yang Anda Masukkan Tidak Valid")
        
main()
