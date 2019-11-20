def primlister(x):
    primelist = []
    for i in range(3, x, 2):
        count = 0
        for l in range(3, i, 2):
            if i % l == 0:
                count += 1

        if count == 0:
            primelist.append(i)

        else:
            continue
    return primelist
if __name__ == "__main__":
    print(primlister(10000))
