# Praktikum--2-KOMNUM
|    NRP     |           Nama             |
| :--------: |       :------------:       |
| 5025251218 | Mushallina Dzikri Rozana   |
| 5025251228 | Raden Roro Fabronita Sectia Farela                    |

# Laporan Praktikum Komputasi Numerik - 2

## 1. Tujuan Program

Program ini dibuat untuk menghitung nilai integral tentu suatu fungsi menggunakan **Metode Integrasi Romberg**. Metode Romberg merupakan pengembangan dari metode Trapesium yang menggunakan **Ekstrapolasi Richardson** untuk meningkatkan akurasi hasil integral tanpa harus menggunakan jumlah interval yang sangat banyak.

Selain melakukan perhitungan integral, program juga menyediakan antarmuka grafis (GUI), visualisasi grafik, tabel iterasi Romberg, perbandingan dengan metode Trapesium, serta fitur penyimpanan hasil.

---

## 2. Library yang Digunakan

### Tkinter

Digunakan untuk membuat antarmuka pengguna (GUI).

```python
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
```

Fungsinya:

* Input fungsi dan parameter
* Tombol perhitungan
* Menampilkan tabel hasil
* Menyimpan hasil ke file

### SymPy

Digunakan untuk mengubah fungsi yang diketik pengguna menjadi bentuk matematika yang dapat diproses komputer.

```python
import sympy as sp
```

Contoh:

```python
sin(x)+x**2
```

akan diterjemahkan menjadi fungsi matematika yang valid.

### NumPy

Digunakan untuk perhitungan numerik dan pengolahan array.

```python
import numpy as np
```

### Matplotlib

Digunakan untuk menampilkan grafik fungsi dan daerah integral.

```python
import matplotlib
from matplotlib.figure import Figure
```

---

# 3. Fungsi parse_fungsi()

```python
def parse_fungsi(expr_str):
```

Fungsi ini bertugas mengubah input teks dari pengguna menjadi fungsi matematika yang bisa dihitung secara numerik.

Contoh:

Input:

```text
sin(x)+x**2
```

Output:

* Bentuk simbolik SymPy
* Fungsi numerik Python

Langkah kerjanya:

1. Membuat variabel simbolik x.
2. Mendefinisikan fungsi matematika yang diperbolehkan.
3. Menggunakan `sympify()` untuk membaca ekspresi.
4. Menggunakan `lambdify()` untuk mengubahnya menjadi fungsi numerik.

---

# 4. Fungsi trapezoidal()

```python
def trapezoidal(f, a, b, n):
```

Fungsi ini mengimplementasikan **Metode Trapesium Komposit**.

Rumus:

[
I \approx \frac{h}{2}
\left[
f(a)+2\sum f(x_i)+f(b)
\right]
]

dengan

[
h=\frac{b-a}{n}
]

Langkah:

1. Menghitung lebar interval h.
2. Menjumlahkan nilai ujung.
3. Menambahkan titik-titik tengah.
4. Mengalikan dengan rumus trapesium.

Output:

Nilai pendekatan integral.

---

# 5. Fungsi romberg()

```python
def romberg(f, a, b, max_level=10, tol=1e-8):
```

Merupakan inti dari program.

Fungsi ini membentuk tabel Romberg berdasarkan hasil metode Trapesium.

## Tahap 1: Trapesium

Baris pertama tabel:

```python
R[(0,0)]
```

menggunakan:

```python
n = 1
```

Kemudian:

```python
R[(1,0)]
```

menggunakan:

```python
n = 2
```

dan seterusnya:

```python
n = 2^i
```

---

## Tahap 2: Ekstrapolasi Richardson

Rumus:

[
R(i,j)=
\frac{4^jR(i,j-1)-R(i-1,j-1)}
{4^j-1}
]

Pada kode:

```python
R[(i,j)] =
(4**j * R[(i,j-1)]
- R[(i-1,j-1)])
/ (4**j - 1)
```

Tujuan:

Menghilangkan galat (error) dari metode Trapesium sehingga hasil menjadi jauh lebih akurat.

---

## Tahap 3: Pemeriksaan Konvergensi

Program menghentikan iterasi jika:

```python
abs(R[(i,i)] - R[(i-1,i-1)]) < tol
```

Artinya selisih dua hasil terakhir sudah lebih kecil dari toleransi yang ditentukan.

Output fungsi:

* Tabel Romberg
* Level konvergen
* Jumlah evaluasi fungsi
* Status konvergensi

---

# 6. Preset Fungsi

```python
PRESET_FUNGSI
```

Berisi beberapa fungsi contoh:

```python
exp(x)
sin(x)
cos(x)
x**2 + 3*x + 1
1/(1+x**2)
sqrt(x)
ln(x+1)
```

Tujuannya memudahkan pengguna mencoba program.

---

# 7. Kelas RombergApp

```python
class RombergApp:
```

Merupakan kelas utama GUI.

Tugasnya:

* Menerima input pengguna
* Menjalankan perhitungan Romberg
* Menampilkan hasil
* Menggambar grafik
* Menyimpan hasil

---

# 8. Panel Input

Fungsi:

```python
_build_input_panel()
```

Digunakan untuk membuat:

### Input fungsi

```python
f(x)
```

### Batas integral

```python
a
b
```

### Toleransi error

```python
tol
```

### Level maksimum

```python
max_level
```

### Tombol

* Hitung Integral
* Reset
* Simpan Hasil

---

# 9. Validasi Input

Fungsi:

```python
_ambil_input()
```

Memastikan:

* Fungsi tidak kosong.
* Nilai a dan b valid.
* a ≠ b.
* Toleransi > 0.
* Level maksimum antara 1–20.

Jika salah, program menampilkan pesan error yang informatif.

---

# 10. Fungsi hitung()

Fungsi utama ketika tombol **Hitung Integral** ditekan.

Langkah kerja:

1. Mengambil input pengguna.
2. Mengubah fungsi menjadi bentuk numerik.
3. Mengecek domain fungsi.
4. Menjalankan metode Romberg.
5. Menampilkan tabel hasil.
6. Menggambar grafik.
7. Menampilkan status konvergensi.
8. Membandingkan dengan metode Trapesium.

---

# 11. Menampilkan Tabel Romberg

Fungsi:

```python
_isi_tabel()
```

Menampilkan seluruh tabel:

[
R(0,0)
]

[
R(1,0),R(1,1)
]

[
R(2,0),R(2,1),R(2,2)
]

dan seterusnya.

Tujuannya agar pengguna dapat melihat proses iterasi secara lengkap.

---

# 12. Visualisasi Grafik

Fungsi:

```python
_gambar_grafik()
```

Menampilkan:

* Grafik fungsi f(x)
* Daerah yang diintegralkan
* Sumbu koordinat

Tujuan:

Membantu pengguna memahami representasi geometris dari integral.

---

# 13. Perbandingan dengan Metode Trapesium

Fungsi:

```python
_bandingkan_trapezoidal()
```

Program menghitung berapa banyak pias yang dibutuhkan metode Trapesium agar mencapai akurasi yang sama dengan Romberg.

Tujuan:

Menunjukkan bahwa Romberg lebih efisien dan lebih cepat mencapai hasil yang akurat.

---

# 14. Fitur Reset

Fungsi:

```python
reset()
```

Mengembalikan seluruh input dan output ke kondisi awal.

---

# 15. Fitur Simpan Hasil

Fungsi:

```python
simpan_hasil()
```

Menyimpan hasil perhitungan ke file `.txt` yang berisi:

* Fungsi
* Batas integral
* Toleransi
* Hasil integral
* Level konvergen
* Jumlah evaluasi fungsi
* Status konvergensi

---

# Kesimpulan

Program ini berhasil mengimplementasikan **Metode Integrasi Romberg** untuk menghitung integral tentu dengan tingkat akurasi yang tinggi. Program dilengkapi dengan GUI yang interaktif, validasi input, visualisasi grafik, tabel iterasi, perbandingan dengan metode Trapesium, serta fitur penyimpanan hasil sehingga lebih mudah digunakan dan dipahami oleh pengguna.

