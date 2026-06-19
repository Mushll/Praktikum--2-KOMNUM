# Praktikum--2-KOMNUM
|    NRP     |           Nama             |
| :--------: |       :------------:       |
| 5025251218 | Mushallina Dzikri Rozana   |
| 5025251228 | Raden Roro Fabronita Sectia Farela                    |

# Laporan Praktikum Komputasi Numerik - 2


## 1. Tujuan Program

Program ini dibuat untuk menghitung nilai integral tentu suatu fungsi menggunakan **Metode Integrasi Romberg**. Metode ini merupakan pengembangan dari metode Trapesium yang menggunakan **Ekstrapolasi Richardson** untuk meningkatkan akurasi hasil integral.

Program menerima fungsi matematika dari pengguna, kemudian menghitung integral pada batas yang ditentukan dan menampilkan tabel iterasi Romberg beserta hasil akhirnya. 

---

## 2. Import Library

```python
import math
```

Library `math` digunakan untuk menyediakan fungsi-fungsi matematika seperti:

* sin()
* cos()
* tan()
* exp()
* log()
* sqrt()

yang nantinya dapat digunakan saat pengguna memasukkan fungsi matematika. 

---

## 3. Fungsi `buat_fungsi()`

```python
def buat_fungsi(teks_fungsi):
```

Fungsi ini bertugas mengubah input teks dari pengguna menjadi fungsi matematika yang dapat dihitung oleh program.

Contoh input:

```text
sin(x)
x**2 + 3*x + 1
exp(x)
```

Langkah kerjanya:

1. Mengubah simbol `^` menjadi `**`.
2. Menyediakan daftar fungsi matematika dari library `math`.
3. Menggunakan `eval()` untuk mengevaluasi fungsi sesuai nilai x yang diberikan.

Output dari fungsi ini adalah fungsi `f(x)` yang siap digunakan dalam perhitungan integral. 

---

## 4. Fungsi `trapezoidal()`

```python
def trapezoidal(f, a, b, n):
```

Fungsi ini mengimplementasikan **Metode Trapesium Komposit**.

Rumus yang digunakan:

   $$ I \approx \frac{h}{2}\left[f(a)+2\sum f(x_i)+f(b)\right]$$

dengan:


   $$ h=\frac{b-a}{n}$$


Langkah perhitungan:

1. Menghitung lebar interval (h).
2. Menjumlahkan nilai fungsi pada batas awal dan akhir.
3. Menambahkan nilai fungsi pada titik-titik tengah.
4. Mengalikan hasil dengan rumus trapesium.

Hasil fungsi ini adalah pendekatan nilai integral menggunakan metode Trapesium. 

---

## 5. Fungsi `romberg()`

```python
def romberg(f, a, b, level_maks=5, toleransi=1e-8):
```

Fungsi ini merupakan inti program yang menerapkan **Metode Integrasi Romberg**.

### Langkah 1: Menghitung Trapesium

Pada setiap iterasi:

```python
n = 2 ** i
```

Jumlah interval akan menjadi:

* 1
* 2
* 4
* 8
* 16
* dan seterusnya

Kemudian dihitung nilai integral menggunakan metode Trapesium.

### Langkah 2: Ekstrapolasi Richardson

Nilai Romberg dihitung dengan rumus:


   $$R(i,j)=R(i,j-1)+\frac{R(i,j-1)-R(i-1,j-1)}{4^j-1}$$


Pada program:

```python
nilai_romberg = baris[j - 1] + (baris[j - 1] - R[i - 1][j - 1]) / (4 ** j - 1)
```

Rumus ini digunakan untuk memperbaiki hasil Trapesium sehingga menjadi lebih akurat.

### Langkah 3: Cek Konvergensi

Program menghentikan iterasi jika:

```python
error = abs(R[i][i] - R[i - 1][i - 1])
```

lebih kecil dari toleransi yang diberikan.

Output fungsi ini adalah tabel Romberg yang berisi seluruh hasil iterasi. 

---

## 6. Fungsi `tampilkan_tabel()`

```python
def tampilkan_tabel(R):
```

Fungsi ini digunakan untuk menampilkan tabel hasil iterasi Romberg ke layar.

Informasi yang ditampilkan:

* Jumlah interval (n)
* Nilai Trapesium
* Nilai hasil ekstrapolasi Romberg

Tujuannya agar pengguna dapat melihat proses perbaikan hasil integral pada setiap iterasi. 

---

## 7. Fungsi `main()`

```python
def main():
```

Merupakan fungsi utama program.

Langkah kerjanya:

1. Menampilkan judul program.
2. Meminta input fungsi dari pengguna.
3. Meminta batas integral a dan b.
4. Meminta level maksimum iterasi.
5. Meminta toleransi error.
6. Membentuk fungsi matematika menggunakan `buat_fungsi()`.
7. Menjalankan metode Romberg.
8. Menampilkan tabel hasil.
9. Menampilkan hasil akhir dan kesimpulan. 

---

# Kesimpulan

Program ini mengimplementasikan **Metode Integrasi Romberg** untuk menghitung integral tentu suatu fungsi. Perhitungan dilakukan dengan mengombinasikan metode Trapesium dan Ekstrapolasi Richardson sehingga menghasilkan nilai integral yang lebih akurat dibandingkan metode Trapesium biasa. Program juga menampilkan tabel iterasi untuk memperlihatkan proses konvergensi menuju hasil yang semakin mendekati nilai integral sebenarnya. 

