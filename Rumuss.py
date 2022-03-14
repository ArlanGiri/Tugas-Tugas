# kubus

sisi = int(input("masukan sisi: "))
rumus = sisi**3
print("Hasil dari " + str(sisi) + " pangkat3 adalah " + str(rumus))

# tabung jika tanpa alas yg diketahui

phi = 3.14
r = int(input("masukan jari jari: "))

rumusluas = phi * r * r

l_alas = rumusluas
t = int(input("masukan tinggi: "))

vol = l_alas * t 
print(vol)

# tabung jika luas alas sdh diketahui

l_alas = int(input("masukan luas alas: "))
t2 = int(input("masukan tinggi: "))

vol2 = l_alas * t2

print(vol2)
