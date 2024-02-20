class lingkaran:
    def luasling(self, jari):
        self.jari = jari
        return 3.14*(jari**2)
    
class segitiga:
    def inseg(self):
        self.a = int(input("Masukkan Alas\t : "))
        self.t = int(input("Masukkan tinggi\t : "))
        
    def luasseg(self):
        self.hasilseg = (self.a * self.t) / 2
            
class trapesium:
    def inttra(self):
        self.s1 = int(input("Masukkan Sisi 1\t : "))
        self.s2 = int(input("Masukkan Sisi 2\t : "))
        self.t = int(input("Masukkan Tinggi\t : "))
        
    def luastra(self):
        self.hasiltra = ((self.s1 + self.s2)*self.t)/2
        
class jajar(segitiga):
    def luasjar(self):
        self.hasiljar = self.a * self.t
        
def menu():
    print(" ")
    print("==================== MENU PILIHAN ====================")
    print("|    1. LINGKARAN                                    |")
    print("|    2. SEGITIGA                                     |")
    print("|    3. TRAPESIUM                                    |")
    print("|    4. JAJAR GENJANG                                |")
    print("======================================================")
    
    pilih = int(input("Masukkan Pilihan Anda : "))
    print("")
    if pilih == 1:
        print("----------| Menghitung Luas Lingkaran |----------")
        hasil1 = lingkaran()
        jari = int(input("Masukkan Jari-Jari : "))
        print
        print("Luas Lingkaran Adalah ", hasil1.luasling(jari))
        menu()
    elif pilih == 2:
        print("----------| Menghitung Luas Segitiga |-----------")
        hasil2 = segitiga()
        hasil2.inseg()
        hasil2.luasseg()
        print
        print("Luas Segitiga Adalah ", hasil2.hasilseg)
        menu()
    elif pilih == 3:
        print("----------| Menghitung Luas Trapesium |----------")
        hasil3 = trapesium()
        hasil3.inttra()
        hasil3.luastra()
        print
        print("Luas Trapesium adalah ", hasil3.hasiltra)
        menu()
    elif pilih == 4:
        print("--------| Menghitung Luas Jajar Genjang |--------")
        hasil4 = jajar()
        hasil4.inseg()
        hasil4.luasjar()
        print("Luas Jajar Genjang adalah ", hasil4.hasiljar)
        menu()
    
    else:
        print("!!!!! MASUKKAN PILIHAN YANG BENAR !!!!!")
        menu()
        
nama = input("\nMasukkan Nama Kamu : ")
print("Hai saya ", nama)

menu()