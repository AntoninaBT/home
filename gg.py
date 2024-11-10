numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # list
primes = []
not_primes = []
for i in range(len(numbers)):
    print(i)
#
for i in range(len(numbers)):
    if i == 1:
        continue
        for j in (2, i):
            if i % j == 0:
                not_primes.append(i)
        else:
            primes.append(i)
    print(primes)
    print(not_primes)