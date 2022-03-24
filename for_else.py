
for n in range(10, 20):      # range[10,20)
    for i in range(2, n):
        if n % i == 0:
            k = n/i
            print(n, "=", k, "*", i)
            break
    else:                            # executing after for sentence finished without being break
        print(n, "is a prime")

