
select = input("""select 
+ untuk penjumlahan
- untuk pengurangan
* untuk perkalian
/ untuk pembagian : """)
 

x = int(input("masukan angka: "))
y = int(input("masukan angka ke2: "))

penjumlahan = x + y 
pengurangan = x - y
perkalian = x * y
pembagian = x / y 

if select == "+":
    print("hasil "+str(x)+" + "+str(y)+" : "+str(penjumlahan))

elif select == "-": 
    print("hasil "+str(x)+" + "+str(y)+" : "+str(pengurangan))
elif select == "*":
    print("hasil "+str(x)+" + "+str(y)+" : "+str(perkalian))
elif select == "/":
    print("hasil "+str(x)+" + "+str(y)+" : "+str(pembagian))
