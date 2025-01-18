def collatz(number):
    """A function used to simulate the collatz sequence."""
    if number % 2 == 0:
        val = number/2
        print(val)
    else:
        val = (3 * number) + 1
        print(val)
    return val

num = int(input("Enter a number: "))

x = collatz(num)

while x != 1:
    x = collatz(x)