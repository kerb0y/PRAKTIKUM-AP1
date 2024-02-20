def biodata():
    print("\n---------------------- BIODATA MAHASISWA ----------------------")
    nama = input("Masukkan Nama\t: ")
    kelas = input("Masukkan Kelas\t: ")
    npm = input("Masukkan NPM\t: ")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Nama anda adalah ", nama)
    print("Anda berasal dari kelas ", kelas)
    print("NPM anda adalah ", npm)
    print()
    
def luas_persegiPanjang():
    print("\n-------------------- LUAS PERSEGI PANJANG ---------------------")
    p = int(input("Masukkan Panjang\t: "))
    l = int(input("Masukkan Tinggi\t\t: "))
    luas = p * l
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(f"Luas Persegi Panjang adalah {luas} cm")
    
def main():
    print("===============================================================")    
    print("                         ACTIVITY 2                            ")
    print("===============================================================")
    biodata()
    luas_persegiPanjang()

main()    
    
    