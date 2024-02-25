import sys
sys.stdin = open('input1.txt', 'r')
sys.stdout = open('output1.txt', 'w')

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

def targetSumNtwoPointer(length, target, arr):
    pointer1 = 0
    pointer2 = len(arr)-1
    while pointer1<pointer2:
        if pointer2 > len(arr)-1 or pointer2 > len(arr)-1:
            break
        if arr[pointer1] + arr[pointer2] == target:
            return f"{pointer1+1} {pointer2+1}"
        if arr[pointer1] + arr[pointer2] < target:
            pointer1 += 1
        if arr[pointer1] + arr[pointer2] > target:
            pointer2 += 1
    return "IMPOSSIBLE"

if __name__ == "__main__":
    length, target = tuple(map(int, input().split(" ")))
    arr = tuple(map(int, input().split(" ")))
    result = targetSumN2(length, target, arr)
    # result = targetSumN(length, target, arr)
    # result = targetSumNtwoPointer(length, target, arr)
    print(result)