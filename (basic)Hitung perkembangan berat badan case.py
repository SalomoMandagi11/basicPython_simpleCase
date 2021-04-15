"""
    Case 1:
    Buat sebuah sistem yang akan membantu menghitung perkembangan tinggi anak.

    Yang akan digunakan:
    1. String
    2. List
    3. Append()
    4. Input()
    5. Integer
    6. If elif
"""

print("Selamat datang di program menghitung perkembangan berat badan anak^-^")
print('\n')
print("Silahkan mengisi beberapa pertanyaa berikut ini: ")

berat_sekarang = int(input("Berapa berat badan anak anda sekarang? "))
berat_dulu = int(input("Berapa berat badan anak anda sebelumnya? "))

perubahan_beratBadan = berat_sekarang - berat_dulu
print("\nPerubahan berat badan anak anda: ", perubahan_beratBadan, " kg\n")

if perubahan_beratBadan > 0:
    print("Berat badan anak anda bertambah, mohon untuk tetap menjaga nutrisi ya^-^")
elif perubahan_beratBadan < 0:
    print("Berat badan anak anda berkurang, mohon perbanyak nutrisi ya^-^")
else:
    print("Berat badan anak anda konstan, mohon pertahankan konsumsi nutrisi yang baik ya ^-^")
