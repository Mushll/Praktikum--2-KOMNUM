import math

def buat_fungsi(teks_fungsi):
    teks_fungsi = teks_fungsi.replace("^", "**")

    daftar_fungsi = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "exp": math.exp,
        "log": math.log,
        "ln": math.log,
        "sqrt": math.sqrt,
        "abs": abs,
        "pi": math.pi,
        "e": math.e,
    }

    def f(x):
        data = daftar_fungsi.copy()
        data["x"] = x
        return eval(teks_fungsi, {"__builtins__": {}}, data)

    return f


def trapezoidal(f, a, b, n):
    h = (b - a) / n
    jumlah = f(a) + f(b)

    for i in range(1, n):
        x_i = a + i * h
        jumlah += 2 * f(x_i)

    return (h / 2) * jumlah


def romberg(f, a, b, level_maks=5, toleransi=1e-8):
    R = []

    for i in range(level_maks):
        baris = []
        n = 2 ** i

        nilai_trap = trapezoidal(f, a, b, n)
        baris.append(nilai_trap)

        for j in range(1, i + 1):
            nilai_romberg = baris[j - 1] + (baris[j - 1] - R[i - 1][j - 1]) / (4 ** j - 1)
            baris.append(nilai_romberg)

        R.append(baris)

        if i > 0:
            error = abs(R[i][i] - R[i - 1][i - 1])
            if error < toleransi:
                break

    return R


def tampilkan_tabel(R):
    print("\nTABEL ROMBERG")
    print("-" * 70)

    for i in range(len(R)):
        n = 2 ** i
        print(f"n = {n:<4}", end="")

        for nilai in R[i]:
            print(f"{nilai:>15.8f}", end="")

        print()


def main():
    print("PROGRAM INTEGRASI ROMBERG SEDERHANA")
    print("Contoh fungsi: exp(x), sin(x), x**2 + 3*x + 1")
    print()

    teks_fungsi = input("Masukkan fungsi f(x)     : ")
    a = float(input("Masukkan batas bawah a   : "))
    b = float(input("Masukkan batas atas b    : "))
    level_maks = int(input("Masukkan level maksimum  : "))
    toleransi = float(input("Masukkan toleransi error : "))

    f = buat_fungsi(teks_fungsi)
    R = romberg(f, a, b, level_maks, toleransi)

    tampilkan_tabel(R)

    hasil_romberg = R[-1][-1]
    hasil_trap_awal = R[0][0]
    hasil_trap_akhir = R[-1][0]

    print("\nHASIL")
    print("-" * 70)
    print(f"Fungsi                 : f(x) = {teks_fungsi}")
    print(f"Batas integral         : {a} sampai {b}")
    print(f"Hasil Trapezoidal awal : {hasil_trap_awal:.10f}")
    print(f"Hasil Trapezoidal akhir: {hasil_trap_akhir:.10f}")
    print(f"Hasil Romberg          : {hasil_romberg:.10f}")

    print("\nKESIMPULAN")
    print("Metode Romberg memperbaiki hasil Trapezoidal dengan ekstrapolasi.")
    print("Jadi, hasil bisa lebih akurat tanpa harus memakai interval yang sangat banyak.")


if __name__ == "__main__":
    main()
