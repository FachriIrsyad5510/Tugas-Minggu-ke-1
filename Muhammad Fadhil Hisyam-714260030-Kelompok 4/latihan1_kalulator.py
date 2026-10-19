print("==================================")
print("KALKULATOR konsol sederhana")
print("==================================")
print("Pilih tersedia: +| -| *| /")
print("----------------------------------")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
operator = input("Masukkan operator (+| -| *| /): ")

print("----------------------------------")

if operator == "+":
    hasil = angka1 + angka2
    print(f"Hasil: {angka1} + {angka2} = {hasil}")

elif operator == "-":   
    hasil = angka1 - angka2
    print(f"Hasil: {angka1} - {angka2} = {hasil}")

elif operator == "*":
    hasil = angka1 * angka2
    print(f"Hasil: {angka1} * {angka2} = {hasil}")

elif operator == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"Hasil: {angka1} / {angka2} = {hasil}")
    else:
        print("Kesalahan: Bilangan tidak dapat dibagi dengan nol.")
else:
        print(f"Operator |{operator}| tidak kenali")
        print("gunakan operator yang tersedia: +| -| *| /")

print("----------------------------------")
print("Terima kasih telah menggunakan kalkulator ini.")