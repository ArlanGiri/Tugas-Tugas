

select = input("""KETIKLAH
 Prisma Untuk menghitung Volume Prisma
 Tabung Untuk menghitung Volume Tabung
 Kubus Untuk menghitung Kubus: """)

if select == "Prisma" :
    alasSegitiga = int(input("masukan alas segitga: "))
    tinggiSegitiga = int(input("masukan tnggi segitga: "))
    setengah = 0.5
    tinggiprisma = int(input("masukan tinggi prisma: "))

    rumus1 = alasSegitiga * tinggiSegitiga
    rumus2 = rumus1 * setengah 
    hasilprism = rumus2 * tinggiprisma
    print("hasil dari", "(",alasSegitiga,"*", tinggiSegitiga, "*",setengah , ")", "*",tinggiprisma, "adalah", hasilprism)
elif select == "Tabung" :
    phi = 3.14
    r = int(input("Masukkan jari-jari: "))
    t = int(input("Masukkan tinggi: "))

    rumus = phi * r * r * t
    print("hasil dari",phi,"*",t,"*",r, rumus)
elif  select == "Kubus":
    sisi = int(input("masukan sisi: "))
    rumuskub = sisi**3
    print("Hasil dari " + str(sisi) + " pangkat3 adalah " + str(rumuskub))




