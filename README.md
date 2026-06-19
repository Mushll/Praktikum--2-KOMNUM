# Praktikum--2-KOMNUM

|     NRP    |                Nama                |
| :--------: | :--------------------------------: |
| 5025251218 |      Mushallina Dzikri Rozana      |
| 5025251228 | Raden Roro Fabronita Sectia Farela |

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

$$ I \approx \frac{h}{2}\left[f(a)+2\sum f(x_i)+f(b)\right] $$

dengan:

$$ h=\frac{b-a}{n} $$

Langkah perhitungan:

1. Menghitung lebar interval (h).
2. Menjumlahkan nilai fungsi pada batas awal dan akhir.
3. Menambahkan nilai fungsi pada titik-titik internal di antara batas awal dan batas akhir dengan bobot 2.
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

## 8. Pengujian Program

Untuk memastikan program berjalan dengan benar, dilakukan pengujian menggunakan fungsi:

$$ f(x) = e^x $$

dengan batas integral:

$$ a = 0, \quad b = 4 $$

Input yang diberikan ke program adalah:

```text
Masukkan fungsi f(x)     : exp(x)
Masukkan batas bawah a   : 0
Masukkan batas atas b    : 4
Masukkan level maksimum  : 6
Masukkan toleransi error : 1e-8
```

Secara analitik, nilai integral dari fungsi tersebut adalah:

$$ \int_0^4 e^x dx = e^4 - e^0 $$

$$ = 53.5981500331 $$

Hasil output akhir dari program adalah:

```text
Hasil Trapezoidal awal : 111.1963000663
Hasil Trapezoidal akhir: 53.6679211235
Hasil Romberg          : 53.5981500334
```

Dari hasil tersebut dapat dilihat bahwa nilai Romberg sangat dekat dengan hasil analitik, yaitu:

```text
Hasil analitik : 53.5981500331
Hasil Romberg  : 53.5981500334
```

Selisih antara hasil analitik dan hasil Romberg sangat kecil, sehingga dapat disimpulkan bahwa algoritma pada program sudah berjalan dengan benar.

Selain itu, hasil Trapezoidal awal masih memiliki kesalahan yang besar karena hanya menggunakan 1 interval. Setelah jumlah interval diperbanyak dan dilakukan Ekstrapolasi Richardson pada metode Romberg, hasil integral menjadi semakin mendekati nilai sebenarnya.

---

## 9. Keterbatasan Program

Program ini sudah dapat menghitung integral tentu dengan metode Romberg, tetapi masih memiliki beberapa keterbatasan, yaitu:

1. Program masih menggunakan antarmuka berbasis terminal atau console.
2. Input batas bawah dan batas atas harus berupa angka, sehingga nilai seperti `pi` belum bisa langsung dimasukkan sebagai batas integral.
3. Fungsi yang dimasukkan harus menggunakan format Python, misalnya `x**2` untuk menyatakan (x^2).
4. Program belum menampilkan grafik fungsi atau visualisasi luas daerah integral.

Meskipun masih sederhana, program sudah memenuhi fungsi utama, yaitu menerima input fungsi, batas integral, level maksimum, dan toleransi error, lalu menghitung nilai integral menggunakan metode Romberg.

---

# Kesimpulan

Program ini berhasil mengimplementasikan **Metode Integrasi Romberg** untuk menghitung nilai integral tentu suatu fungsi. Perhitungan dilakukan dengan mengombinasikan metode Trapesium Komposit dan Ekstrapolasi Richardson.

Berdasarkan pengujian menggunakan fungsi ( f(x) = e^x ) pada interval 0 sampai 4, hasil Romberg yang diperoleh adalah 53.5981500334. Nilai tersebut sangat mendekati hasil analitik, yaitu 53.5981500331. Hal ini menunjukkan bahwa program sudah menghasilkan output yang valid.

Metode Romberg terbukti lebih akurat dibandingkan Trapezoidal biasa karena hasil integral dapat diperbaiki melalui tabel iterasi Romberg. Dengan demikian, kelemahan metode Trapezoidal yang membutuhkan banyak interval untuk mencapai akurasi tinggi dapat dikurangi.

Program ini juga cukup fleksibel karena pengguna dapat memasukkan fungsi, batas integral, level maksimum, dan toleransi error sesuai kebutuhan. Namun, program masih berbasis terminal sehingga tampilan antarmukanya masih sederhana.
