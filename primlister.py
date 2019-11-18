def primelister(x):
    primlist = [2]
    for i in range(3,x+1):
        count = 0
        if i % 2 == 0:
            pass
        else:
            for l in range(2, i):
                if l**(x-1) % x == 1:
                    count=count+1
                    if count == len(range(2, i)):
                        primlist.append(i)
                    else:
                        break
    return primlist
if __name__ == "__main__":
    print(primelister(45))
