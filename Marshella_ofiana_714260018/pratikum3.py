# =========================================
# PRATIKUM 3: DERET ARITMATIKA & AKUMULATOR
# Simpan sebagai: pratikum_03.py
# =========================================

print("=== PROGRAM HITUNG DERET ARITMATIKA ===")

awal = int(input("Masukkan suku pertama (a): "))
beda = int(input("Masukkan beda deret    (b): "))

# 1. IMPLEMENTASI WHILE: Validasi input jumlah suku agar harus positif (> 0)
banyak = int(input("Masukan banyak suku (n): "))
while banyak <=0:
    print("peringatan: Banyak suku harus lebih dari 0!")
banyak = int(input("silahkan masukkan ulang suku (n): "))

# 2. IMPLEMENTASI FOR & AKUMULATOR: Mencetak deret dan menjumlahkan totalnya
suku= awal
total = 0 # Celengan Akumulator

print("barisan deret: ", end="")
for i in range (banyak):
    print(suku, end="")
    total += suku #Akumulasi penjumlahan bertahap
    suku += beda # Menyiapkan suku berikutnya

print(f"total jumlah seluruh deret = {total}")

