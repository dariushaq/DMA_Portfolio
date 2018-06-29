import sys
import math

def add():
    x = int(sys.argv[2])
    y = int(sys.argv[3])
    print(x + y)

def sub():
    x = int(sys.argv[2])
    y = int(sys.argv[3])
    print(x - y)

def mult():
    x = int(sys.argv[2])
    y = int(sys.argv[3])
    print(x * y)

def div():
    x = int(sys.argv[2])
    y = int(sys.argv[3])
    print(x / y)

def count():
    x = (int(sys.argv[2]) + 1)
    for i in range(1, x):
        print(i)

def pythag(a, b):
    a_sq = math.pow(a, 2)
    b_sq = math.pow(b, 2)
    return math.sqrt(a_sq + b_sq)

def square():
    x = int(sys.argv[2])
    return math.pow(x, 2)

def power():
    x = int(sys.argv[2])
    y = int(sys.argv[3])
    return math.pow(x, y)

def sqrt():
    x = int(sys.argv[2])
    return math.sqrt(x)

def quad_f():
    a = int(sys.argv[2])
    b = int(sys.argv[3])
    c = int(sys.argv[4])
    return ((((0 - b) + math.sqrt(math.pow(b, 2)) - 4 * a * c)) / (2 * a))

def main():
    command = sys.argv[1]
    if command == "add":
        add()
    elif command == "subtract":
        sub()
    elif command == "multiply":
        mult()
    elif command == "divide":
        div()
    elif command == "count_to":
        count()
    elif command == "hypot":
        a = int(sys.argv[2])
        b = int(sys.argv[3])
        pythag(a, b)
    elif command == "square":
        square()
    elif command == "power":
        power()
    elif command == "sqrt":
        sqrt()
    elif command == "quadratic":
        quad_f()
    else:
        print("invalid")

if __name__ == "__main__":
    main()
