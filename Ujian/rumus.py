# rumus.py

# Kelas Persegi
class Persegi:
    # Metode untuk menghitung luas persegi
    def luas(self, sisi):
        return sisi * sisi
    # Metode untuk menghitung keliling persegi
    def keliling(self, sisi):
        return 4 * sisi

# Kelas Persegi Panjang
class PersegiPanjang:
    # Metode untuk menghitung luas persegi panjang
    def luas(self, p, l):
        return p * l
    # Metode untuk menghitung keliling persegi panjang
    def keliling(self, p, l):
        return 2 * (p + l)

# Kelas Segitiga
class Segitiga:
    # Metode untuk menghitung luas segitiga
    def luas(self, a, t):
        return 0.5 * a * t
    # Metode untuk menghitung keliling segitiga
    def keliling(self, sisi):
        return 3 * sisi