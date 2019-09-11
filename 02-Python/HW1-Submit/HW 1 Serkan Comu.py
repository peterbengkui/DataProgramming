import numpy as np

# Problem 1
def operate(a, b, term):
    if term == "add":
        return a + b
    if term == "multiply":
        return a * b
    else:
        return "Bad String"


print(operate(4, 4, "add"))
print(operate(4, 4, "multiply"))
print(operate(4, 4, "negative"))


# Problem 2
def Fibonacci(N):
    Fib = [1, 1]
    n = 1
    for i in range(n, N):
        Fib.append(Fib[-1] + Fib[-2])
    return Fib


print(Fibonacci(5))
print(Fibonacci(10))
print(Fibonacci(20))
print(Fibonacci(50))

#Problem 3
#Maybe easier way to do?
def decode(Letter):
    if Letter == "A" or Letter == "a":
        return '1'
    if Letter == "B" or Letter == "b":
        return '2'
    if Letter == "C" or Letter == "c":
        return '3'
    if Letter == "D" or Letter == "d":
        return '4'
    if Letter == "E" or Letter == "e":
        return '5'
    if Letter == "F" or Letter == "f":
        return '6'
    if Letter == "G" or Letter == "g":
        return '7'
    if Letter == "H" or Letter == "h":
        return '8'
    if Letter == "I" or Letter == "i":
        return '9'
    if Letter == "J" or Letter == "j":
        return '10'
    if Letter == "K" or Letter == "k":
        return '11'
    if Letter == "L" or Letter == "l":
        return '12'
    if Letter == "M" or Letter == "m":
        return '13'
    if Letter == "N" or Letter == "n":
        return '14'
    if Letter == "O" or Letter == "o":
        return '15'
    if Letter == "P" or Letter == "p":
        return '16'
    if Letter == "Q" or Letter == "q":
        return '17'
    if Letter == "R" or Letter == "r":
        return '18'
    if Letter == "S" or Letter == "s":
        return '19'
    if Letter == "T" or Letter == "t":
        return '20'
    if Letter == "U" or Letter == "u":
        return '21'
    if Letter == "V" or Letter == "v":
        return '22'
    if Letter == "W" or Letter == "w":
        return '23'
    if Letter == "X" or Letter == "x":
        return '24'
    if Letter == "Y" or Letter == "y":
        return '25'
    if Letter == "Z" or Letter == "z":
        return '26'

    else:
        return '999'


def Encode(String):
    encoded= []
    for i in range (0,len(String)):
        encoded.append(decode(String[(i)]))
    return '.'.join(encoded)


print(Encode("Aab"))
print(Encode("I Love"))
print(Encode("I Love You"))
print(Encode("William Salas"))
print(Encode("I am so dumb"))


def get_n(N):
    sum=1
    S=2
    while N>sum:
        sum=sum+(1/S)
        S+=1

    return (S-1)

print(get_n(5))
print(get_n(4))
print(get_n(7))

def describe(list):
    print("The number of elements of this list is ",len(list))
    print('The mean of this list is ',(sum(list)/len(list)))
    print('The variance of this list is ', np.var(list))
    print('The standard deviation of this list is ', np.std(list))

  #  number of elements
   # mean
   # variance
   # standard deviation

describe([1,5,43,6,3,2,7,23])