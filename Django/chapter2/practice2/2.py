def do():
    number = [i for i in range(1,11)]
    print(number)
    for n in number:
        if n == 5:
            continue
        elif n == 8:
            break
        print(n)

do()