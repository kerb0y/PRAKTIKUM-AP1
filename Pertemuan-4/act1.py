print ("\n==============================================")
print ("                PROGRAM KALKULATOR              ")
print ("\n==============================================")

nama = input("Masukkan Nama\t\t: ")
kelas = input("Masukkan Kelas\t\t: ")
a = float(input("Masukkan Bilangan A\t\t: "))
b = float(input("Masukkan Bilangan B\t\t: "))

print("")

tambah = a + b
kurang = a - b
kali = a * b
bagi = a / b

print ("\n==============================================")
print ("                HASIL KALKULASI                 ")
print ("\n==============================================")
print ("Hai ", nama, " dari kelas ", kelas, " ini hasil kalkulasi kamu\n")
print (a, " + ", b, " = ", tambah)
print (a, " - ", b, " = ", kurang)
print (a, " * ", b, " = ", kali)
print (a, " / ", b, " = ", bagi)


