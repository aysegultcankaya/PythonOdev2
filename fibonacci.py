# İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.
n = int(input("Kaç elemanlı fibonacci serisi oluşturmak istersiniz? "))
while n<20:
    n = int(input("20'den büyük değer giriniz:"))

x, y = 1, 1
fib =[]
for _ in range(n):
    fib.append(x)
    x , y = y, x + y
print (fib)    
    
