# Nomer 1

bilangan = int(input("Masukan Angka atau Bilagan : "))
rumus1 = bilangan%3
if rumus1 == 0 :
    print("Bilangan yg anda masukan habis dibagi 3")
else :
    print("Bilangan yg anda masukan tidak habis dibagi 3")

# nomer2

nama = input("Masukan nama anda: ")
gender = input("Apakah anda Pria/Wanita? ")
gpria = "Pria"
gwan = "Wanita"

if gender == gpria :
    print("Halo bro", nama)
elif gender == gwan :
    print("Halo sis", nama)
else :
    print("Lho Rak Nggenah")

# nomer3

nama2 = input("Siapa Nama anda? ")
tanggallahir = int(input("Kapan Anda lahir? "))
if tanggallahir < 1944 :
    print("what??")
elif tanggallahir <= 1964 :
    print(nama2, ",Berdasarkan tanggal lahir Anda. Anda termasuk generasi Baby Boomer")
elif tanggallahir <= 1979 :
    print(nama2, ",Berdasarkan tanggal lahir Anda. Anda termasuk Generasi X")
elif tanggallahir <= 1994 :
    print(nama2,",Berdasarkan tanggal lahir Anda. Anda termasuk Generasi Y (Millenials)")
elif tanggallahir <= 2015 :
    print(nama2,",Berdasarkan tanggal lahir Anda. Anda termasuk Generasi Z")
else  :
    print("Anak-Anak")
