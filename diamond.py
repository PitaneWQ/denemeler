harf = input("Bir harf giriniz: ")
sayi = int(input("Sayı giriniz: "))
hnum = 1
nnum = sayi

for l in range(sayi):
    print("."*nnum+harf*hnum+"."*nnum)
    hnum +=2
    nnum -=1

for l in range(sayi):
    print("."*nnum+harf*hnum+"."*nnum)
    hnum -=2
    nnum +=1
print("."*nnum+harf*hnum+"."*nnum)
