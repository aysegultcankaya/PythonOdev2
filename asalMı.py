#Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.

sayi=int(input("Bir sayı giriniz="))

asalMi=True

if (sayi==1):
    print("Sayı asal değildir.")

for i in range(2,sayi):
    if (sayi%i==0):
        asalMi=False
        break

if asalMi:
    print(f'{sayi} bir asal sayıdır.')
else:
    print(f'{sayi} bir asal sayı değildir.')