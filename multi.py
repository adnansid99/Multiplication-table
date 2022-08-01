while True:
    a = 0
    intoSy = "×"
    eq = "="
    num = int(input("\nEnter value: "))
    theSum = ((num * 10) + 1)
    for i in range(num, theSum, num):
        a = a + 1
        print("{} {} {} {} {}".format(num, intoSy, a, eq, i))
