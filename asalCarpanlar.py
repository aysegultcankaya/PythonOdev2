#Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 

sayi = int(input("Bir sayı girin: "))
i = 2
print(sayi, "sayısının asal çarpanları:")
while i <= sayi:
    if sayi % i == 0:
        print(i)
        sayi //= i
    else:
        i += 1