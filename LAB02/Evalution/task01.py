import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def targetSumN2(length, target, arr):
    for i in range(length):
        for j in range(i+1, length):
            if arr[i] + arr[j] == target:
                return f"{i+1} {j+1}"
    return "IMPOSSIBLE"

def targetSumN(length, target, arr):
    cache = {}
    newArr = []

    for i in range(length):
        newArr.append((i, arr[i]))

    for i, value in newArr:
        remaining = target - arr[i]
        if remaining in cache:
            return f"{cache[remaining]+1} {i+1}"
        cache[value] = i
    return "IMPOSSIBLE"


def main1():
    testCase = int(input())
    for _ in range(testCase):
        length, target = tuple(map(int, input().split(" ")))
        arr = tuple(map(int, input().split(" ")))
        result = targetSumN2(length, target, arr)
        print(result)
def main2():
    testCase = int(input())
    for _ in range(testCase):
        length, target = tuple(map(int, input().split(" ")))
        arr = tuple(map(int, input().split(" ")))
        result = targetSumN(length, target, arr)
        print(result)

def main3():
    testCase = int(input())
    for _ in range(testCase):
        length, target = tuple(map(int, input().split(" ")))
        arr = tuple(map(int, input().split(" ")))
        result = targetSumN(length, target, arr)
        print(result)

if __name__ == "__main__":
    # main1()
    main2()