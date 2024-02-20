def main():
    file = open('bintang.txt', 'w')
    
    nama = input('\nMasukkan Nama\t\t= ')
    kelas = input('\nMasukkan Kelas\t\t= ')
    npm = input('\nMasukkan NPM\t\t= ')
    jurusan = input('\nMasukkan Jurusan\t= ')
    fakultas = input('\nMasukkan Fakultas\t= ')
    angkatan = input('\nMasukkan Angkatan\t= ')
    
    file.write(nama + '\n')
    file.write(kelas + '\n')
    file.write(npm + '\n')
    file.write(jurusan + '\n')
    file.write(fakultas + '\n')
    file.write(angkatan + '\n')
    
    file.close()
    print('\nData Berhasil Ditulis')
main()