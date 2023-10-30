#Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.


sayi1 = int(input("Birinci sayıyı giriniz:"))
sayi2 = int(input("İkinci sayıyı giriniz:"))

if sayi1 > sayi2: 
    small = sayi2 
else: 
    small = sayi1 
for i in range(1, small+1): 
        if((sayi1 % i == 0) and (sayi2 % i == 0)): 
            ebob = i
            
ekok = int((sayi1*sayi2)/ebob)

print("Girdiğiniz sayıların EBOB değeri:",ebob)
print("Girdiğiniz sayıların EKOK değeri :",ekok )