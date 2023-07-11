def prime_factorizer(number):
    factors = []
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)

    if number > i:
        factors.append(number)

    return factors


number = int(input("Enter number to calculate prime factors:\t"))
print(prime_factorizer(number))
