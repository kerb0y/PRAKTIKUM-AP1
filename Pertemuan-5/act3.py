def main():
    
    print()
    file = open('bintang.txt', 'r')
    
    isi_file = file.read()
    
    file.close()
    print('Data Berhasil Dibaca\n')
main()