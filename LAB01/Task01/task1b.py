import sys
sys.stdin = open('input1b.txt', 'r')
sys.stdout = open('output1b.txt', 'w')


def calculate(str):
    arr = str.split(" ")

    operator1 = int(arr[1])
    operand = arr[2]
    operator2 = int(arr[3])
    result = ""

    if operand == "+":
        result = operator1 + operator2
    elif operand == "-":
        result = operator1 - operator2
    elif operand == "*":
        result = operator1 * operator2
    elif operand == "/":
        result = operator1 / operator2
    return f"The result of {operator1} {operand} {operator2} is {result}"


if __name__ == "__main__":
    testCase = int(input())
    for c in range(testCase):
        print(calculate(input()))