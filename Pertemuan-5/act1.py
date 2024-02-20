print ()

nolist = []
ganjil = []
genap = []

data = int(input("Masukkan Jumlah Elemen Dalam List = " ) )

for i in range(1, data + 1):
    elm = int(input(f"Nilai elemen ke {i} : "))
    nolist.append(elm)
    
for j in range(data):
    if nolist[j] % 2 == 0:
        genap.append(nolist[j])
    else:
        ganjil.append(nolist[j])
print()

print("Elemen-elemen dalam list = ", nolist)
print("Elemen ganjil dalam list = ", ganjil)
print("Elemen genap dalam list = ", genap)