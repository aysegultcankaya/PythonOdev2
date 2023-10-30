#Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.

sayi=int(input("Sayı giriniz: "))
s=0
for i in range(1,sayi):
    if(sayi%i==0):
        s=s+i
if(s==sayi):
    print(f"{sayi} sayısı mükemmel sayıdır.")
else:
    print(f"{sayi} sayısı mükemmel sayı değildir.")