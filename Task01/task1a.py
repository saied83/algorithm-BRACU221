import sys
sys.stdin = open('input1a.txt', 'r')
sys.stdout = open('output1a.txt', 'w')


def findOddEven(number):
    if number %2 == 0:
        print(f'{number} is an Even number.')
    else:
        print(f'{number} is an Odd number.')



if __name__ == "__main__":
    testCase = int(input())
    for c in range(testCase):
        findOddEven(int(input()))