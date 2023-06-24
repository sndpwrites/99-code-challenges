def fizz_buzz(size):
    for i in range(1, size+1):
        if (i % 3 == 0) & (i % 5 == 0):
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizz_buzz(100)
