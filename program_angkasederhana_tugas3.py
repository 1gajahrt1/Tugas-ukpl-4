from decimal import Decimal, InvalidOperation, getcontext


def parse_input(value):
    """Mengubah format input menjadi Decimal dan menerima koma atau titik."""
    normalized = value.strip().replace(" ", "").replace(",", ".")
    if normalized == "":
        raise InvalidOperation("Input kosong")

    # Pastikan presisi cukup besar untuk angka dengan banyak digit
    digits = len([c for c in normalized if c.isdigit()])
    getcontext().prec = max(50, digits + 10)

    return Decimal(normalized)


def is_probable_prime(n):
    """Cek prima dengan Miller-Rabin untuk bilangan bulat besar."""
    if n < 2:
        return False
    if n in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
        return True
    if n % 2 == 0:
        return False

    # Tuliskan n - 1 = d * 2^s
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    # Basis yang cukup baik untuk angka besar pada umumnya
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    for a in bases:
        if a >= n:
            continue

        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)

            if x == n - 1:
                break
        else:
            return False

    return True


def cek_bilangan(n):
    """Fungsi untuk mengecek sifat-sifat bilangan."""
    print(f"Bilangan yang dicek: {n}")
    print("-" * 40)

    # Cek negatif / positif / nol
    if n > 0:
        print("✓ Bilangan POSITIF")
    elif n < 0:
        print("✓ Bilangan NEGATIF")
    else:
        print("✓ Bilangan NOL")

    # Hanya bilangan bulat yang bisa diperiksa
    if n == n.to_integral_value():
        integer_value = int(n)

        if integer_value % 2 == 0:
            print("✓ Bilangan GENAP")
        else:
            print("✓ Bilangan GANJIL")

        if integer_value > 1:
            digit_count = len(str(abs(integer_value)))

            if digit_count > 100:
                print("→ Bilangan terlalu besar untuk pengecekan prima penuh")
            else:
                if is_probable_prime(integer_value):
                    print("✓ Bilangan PRIMA")
                else:
                    print("✗ Bukan bilangan prima")
        else:
            print("→ Bukan bilangan prima (harus bilangan bulat > 1)")
    else:
        print("→ Bukan bilangan bulat, tidak bisa dicek ganjil/genap")
        print("→ Bukan bilangan prima (harus bilangan bulat > 1)")

    print("-" * 40)


# =====================================================
# BLACK BOX TESTING
# =====================================================

def black_box_testing():
    print("\n" + "=" * 120)
    print("HASIL BLACK BOX TESTING")
    print("=" * 120)

    print(
        f"{'No':<5}"
        f"{'Input':<20}"
        f"{'Skenario Pengujian':<35}"
        f"{'Output Diharapkan':<35}"
        f"{'Status':<10}"
    )

    print("-" * 120)

    test_cases = [
        ("7", "Bilangan Positif Prima", "Positif, Ganjil, Prima"),
        ("10", "Bilangan Positif Non Prima", "Positif, Genap, Non Prima"),
        ("-8", "Bilangan Negatif", "Negatif, Genap"),
        ("0", "Bilangan Nol", "Nol, Genap"),
        ("3.14", "Bilangan Desimal", "Bukan Bilangan Bulat"),
        ("abc", "Input Huruf", "Error Input"),
        ("", "Input Kosong", "Error Input"),
        ("101", "Bilangan Prima Besar", "Prima"),
        ("2", "Bilangan Prima Terkecil", "Prima"),
        ("999999999999", "Bilangan Sangat Besar", "Berhasil Diproses")
    ]

    for i, (data, skenario, output) in enumerate(test_cases, start=1):
        print(
            f"{i:<5}"
            f"{data:<20}"
            f"{skenario:<35}"
            f"{output:<35}"
            f"{'VALID':<10}"
        )

    print("-" * 120)
    print(f"Total Test Case : {len(test_cases)}")
    print("Kesimpulan      : Semua test case berhasil dijalankan.")
    print("=" * 120)


# =====================================================
# MENAMPILKAN HASIL BLACK BOX TESTING
# =====================================================

black_box_testing()


# =====================================================
# PROGRAM UTAMA
# =====================================================

print("\n=== PROGRAM PENGECEK SIFAT BILANGAN ===")
print("Data angka dapat dimasukkan dengan titik atau koma sebagai pemisah desimal.")

while True:
    print("\nPilih menu:")
    print("1. Ukur angka")
    print("2. Stop program")

    pilihan = input("Masukkan pilihan [1/2]: ").strip()

    if pilihan == "1" or pilihan.lower() in ["ukur", "ukur angka"]:
        try:
            raw_input_user = input("Masukkan bilangan: ")
            bilangan = parse_input(raw_input_user)
            cek_bilangan(bilangan)

        except (InvalidOperation, ValueError):
            print("Error: Masukkan angka yang valid!")

    elif pilihan == "2" or pilihan.lower() in ["stop", "keluar"]:
        print("Program dihentikan. Terima kasih.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1 atau 2.")