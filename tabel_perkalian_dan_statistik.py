print("Tabel Perkalian dan Statistik")

n = int(input("n: "))

# Validasi n dengan while
while n <= 0:
    print("n harus lebih dari 0!")
    n = int(input("Masukkan n lagi: "))

# Inisialisasi total keseluruhan dan counter genap
total_keseluruhan = 0
counter_genap = 0

# Nested loop untuk membuat tabel perkalian
for i in range(1, n + 1):
    total_baris = 0

    for j in range(1, n + 1):
        hasil = i * j

        print(hasil, end="\t")

        # Menghitung total baris
        total_baris += hasil

        # Menghitung total keseluruhan
        total_keseluruhan += hasil

        # Menghitung banyak hasil yang genap
        if hasil % 2 == 0:
            counter_genap += 1

    print("| Total baris =", total_baris)

# Menampilkan statistik
print("\nStatistik:")
print("Total keseluruhan =", total_keseluruhan)
print("Jumlah bilangan genap =", counter_genap)