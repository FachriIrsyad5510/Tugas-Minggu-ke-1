#KALKULATOR
print("==================================")
print("MY KALKULATOR")
print("==================================")
print("Operasi Tersedia |+| |-| |*| |/|:")
print("----------------------------------")

#BAGIAN MASUKKAN ANGKA
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
operator = input("Masukkan operator (|+| |-| |*| |/|): ")

#OUTPUT
if operator == "+":
    hasil = angka1 + angka2
    print(f"Hasil penjumlahan: {angka1} + {angka2} = {hasil:.2f}")

elif operator == "-":
    hasil = angka1 - angka2
    print(f"Hasil pengurangan: {angka1} - {angka2} = {hasil:.2f}")

elif operator == "*":
    hasil = angka1 * angka2
    print(f"Hasil perkalian: {angka1} x {angka2} = {hasil:.2f}")

elif operator == "/":
    if angka2 == 0:
        print("Pembagian dengan nol tidak diperbolehkan.")
    else:
        hasil = angka1 / angka2
        print(f"Hasil pembagian: {angka1} / {angka2} = {hasil:.2f}")

else:
    print(f"Operator |{operator}| tidak dikenali.")
    print("Silakan gunakan salah satu operator berikut: |+| |-| |*| |/|")

print("==================================")
print("Terima kasih telah menggunakan kalkulator ini!")