def allprimes(x):
    a = [2]
    if x > 1:
        for l in range(2, x):
            b = 0
            for i in range(2, l):
                if l % i == 0:
                    pass
                else:
                    b = +1
                    if b == len(range(2, l)):
                        a.append(l)
    else:
        print("1den büyük bir sayı giriniz.")
    return a
if __name__ == "__main__":
    x  = int(input("Bir sayı giriniz : "))
    print(allprimes(x))
