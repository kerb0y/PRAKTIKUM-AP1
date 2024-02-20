def main():
    print('---------------\n1. Membuat file\n2. Membaca file\n3. Keluar\n---------------')
    
def write():
    file = open('bintang.txt', 'w')
    
    paragraf1 = input('Masukkan paragraf pertama    = ')
    paragraf2 = input('Masukkan paragraf kedua      = ')
    paragraf3 = input('Masukkan paragraf ketiga     = ')
    
    file.write(paragraf1 + '\n')
    file.write(paragraf2 + '\n')
    file.write(paragraf3 + '\n')
    
    file.close()
    print('---------------------\nData Berhasil Ditulis\n---------------------')
    main()

def read():
    
    print()
    file = open('bintang.txt', 'r')
    isi_file = file.read()
    file.close()
    print('Data Berhasil Dibaca\n')
    
    print('Isi file : ')
    print(isi_file)
    main()
main()

def cls():
    exit(0)

while main:
    choice = int(input('\nPilih menu [1-3] : '))
    if choice == 1:
        write()
    elif choice == 2:
        read()
    elif choice == 3:
        print('\n--- Terima kasih ---')
        cls()
    else:
        print('Input tidak dikenali')