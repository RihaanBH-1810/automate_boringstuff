print("Enter a number :")
n = int(input())

def collatz(number):
    if number%2 == 0:
        print(number//2)
        return number//2
    else:
        print(3 * number + 1)
        return 3 * number + 1

while True:
    n = collatz(n)
    if n == 1:
        break