def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return abs(x) 

num1 = int(input("x"))
num2 = int(input("y"))

if num1 < 0 or num2 < 0:
    print("give me more")
else:
    print("GCD",gcd(num1, num2))