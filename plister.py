def primlisterr(x):
    primelist = []
    for i in range(2, x):
        count = 0
        for l in range(2, i):
            if i % l == 0:
                count += 1

        if count == 0:
            primelist.append(i)

        else:
            continue
    return primelist
if __name__ == "__main__":
    print(primlisterr(10000))
