
x = int(raw_input("Vpisi stevilo od 1 do 100"))

while x >= 1 and x <= 100:

    for x in range(1, x + 1):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")

        elif  x % 3 == 0:
            print("Fizz")

        elif x % 5 == 0:
            print("Buzz")

        else:
            print(x)
    break

else:
    print "ni stevilo od 1 do 100"






