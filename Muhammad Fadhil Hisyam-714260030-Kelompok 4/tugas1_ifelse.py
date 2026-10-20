# ===============================================
# Tugas mandiri modul 1 - Program percabangan
# Nama    : MUHAMMAD FADHIL HISYAM
# Nim     : 714260030
# Kelas   : D4IT 1B
# ===============================================

print("=" * 45)
print("            PROGRAM PERCABANGAN")
print("=" * 45)

grade = input("       Masukkan nilai akhir (0-100): ").strip()
print("-" * 45)

stripReplacer = grade.lstrip("-").replace(".", "", 1)

if grade.count("-") > 1 or not stripReplacer.isdigit():
    print("Input tidak valid! Masukkan angka, bukan huruf atau simbol")
else:
    nilai = float(grade)
    if nilai < 0 or nilai > 100:
        print =(f"Nilai {nilai} Ditolak! Nilai harus berada di angka 0-100 ")
    else:
        if nilai >= 90:
            huruf = "A"
        elif nilai >= 80:
            huruf = "B"
        elif nilai >= 75:
            huruf = "C"
        elif nilai >= 60:
            huruf = "D"
        elif nilai >= 0:
            huruf = "BELAJAR LEBIH GIAT YAAA"
        else:
            huruf = "-"
        if huruf in ("A", "B", "C"):
            keterangan = "LULUS"
        else:
            keterangan = "TIDAK LULUS"

        print(f"Nilai akhir    : {nilai}")
        print(f"Huruf mutu     : {huruf}")
        print(f"Keterangan     : {keterangan}")

print("-" * 45)