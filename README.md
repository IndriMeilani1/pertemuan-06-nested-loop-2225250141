# Pertemuan 06 Nested Loop Python

Nama: Indri Meilani
NIM: 2225250141
Kelas: 3A

## Tujuan
Menggunakan nested loop, pola, akumulasi, dan pencacahan.

## Cara Menjalankan
python3 tugas/tabel_perkalian_dan_statistik.py

## Algoritma Tugas 3
Loop luar berfungsi untuk mengatur baris pada tabel perkalian. Jadi, loop ini menentukan angka pertama yang akan dikalikan. Loop dalam berfungsi untuk mengatur kolom pada setiap baris. Loop ini akan mengalikan angka dari loop luar dengan angka pada loop dalam sampai membentuk tabel perkalian. Akumulator digunakan untuk menyimpan dan menjumlahkan hasil perhitungan secara bertahap. Pada program ini, akumulator digunakan untuk menghitung total setiap baris dan juga total keseluruhan dari tabel perkalian. Counter digunakan untuk menghitung banyaknya hasil perkalian yang memenuhi kondisi tertentu. Pada program ini, counter digunakan untuk menghitung berapa banyak hasil perkalian yang merupakan bilangan genap.

## Hasil Pengujian
input 1, hasil yang diharapkan Jumlah pasangan = 1, total semua = 1, banyak hasil genap = 0, keluaran aktual Jumlah pasangan = 1, total semua = 1, banyak hasil genap = 0, dan status berhasil. input 2, hasil yang diharapkan Jumlah pasangan = 4, total semua = 9, banyak hasil genap = 3, keluaran aktual Jumlah pasangan = 4, total semua = 9, banyak hasil genap = 3, dan status berhasil. input 3, hasil yang diharapkan Jumlah pasangan = 9, total semua = 36, banyak hasil genap = 5, keluaran aktual Jumlah pasangan = 9, total semua = 36, banyak hasil genap = 5, dan status berhasil.

## Analisis Efisiensi
Pada program ini terdapat loop luar dan loop dalam. Loop luar berjalan sebanyak n kali, dan setiap kali loop luar berjalan, loop dalam juga berjalan sebanyak n kali. Jadi, badan loop dalam berjalan sebanyak n × n = n² kali.

## Refleksi
Salah satu kesalahan yang ditemukan pada nested loop adalah posisi perulangan yang kurang tepat, sehingga hasil perkalian yang ditampilkan bisa tidak sesuai dengan jumlah baris dan kolom yang seharusnya. Cara memperbaikinya adalah dengan memastikan loop luar digunakan untuk mengatur baris, sedangkan loop dalam digunakan untuk mengatur kolom. Selain itu, variabel total_baris harus diatur kembali menjadi 0 setiap kali masuk ke baris baru. Dengan begitu, setiap baris dapat dihitung totalnya dengan benar dan hasil tabel perkalian juga sesuai dengan nilai n.
