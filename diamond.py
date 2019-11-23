harf = input("Bir harf giriniz: ")
sayi = 2*(int(input("Sayı giriniz: ")))+1
hnum = 1
nnum = int((sayi-1)/2)

for l in range(int((sayi-1)/2)):
    print("."*nnum+harf*hnum+"."*nnum)
    hnum +=2
    nnum -=1

for l in range(int((sayi-1)/2)):
    print("."*nnum+harf*hnum+"."*nnum)
    hnum -=2
    nnum +=1
print("."*nnum+harf*hnum+"."*nnum)
