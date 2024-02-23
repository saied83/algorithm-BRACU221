import sys
sys.stdin = open('input2.txt', 'r')
sys.stdout = open('output2.txt', 'w')

def findMax(left, right):
    if left > right:
        return left
    else:
        return right

def divideAndFindMax(arr):
    if len(arr) == 1:
        return arr[0]
    mid = len(arr)//2
    left = divideAndFindMax(arr[:mid])
    right = divideAndFindMax(arr[mid:])
    return findMax(left, right)


if __name__ == "__main__":
    testCase = int(input())
    arr = list(map(int, input().split(" ")))
    result = divideAndFindMax(arr)
    print(result)