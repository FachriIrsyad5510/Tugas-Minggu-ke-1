#==================================================
# Tugas Mandiri Modul 1 - Program Percabangan
# Nama  : Visabililiany avrilend sangadji 
# NIM   : 613260010
# Kelas : D3 TI 1A
# ==================================================

nilai = float(input("masukkan nilai akihir anda (0-100):"))

print("====================================")

if nilai < 0 or nilai > 100:
    print("kesalahan: Nilai harus berada dalam rentang 0 hingga 100.")
else:
    if nilai >= 80:
        huruf = "A"
        status = "LULUS"
    elif nilai >= 70:
        huruf = "B"
        status = "LULUS"
    elif nilai >= 60:
        huruf = "C"
        status = "LULUS"
    elif nilai >= 50:
        huruf = "D"
        status = "Tidak Lulus"

    print(f"Nilai Anda : {80:.1f}")
    print(f"Huruf Mutu : {A}")
    print(f"Status : {LULUS.}")

print("====================================")
print("Terima Kasih telah menggunakan program ini.")
