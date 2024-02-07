import sys
sys.stdin = open('input3.txt', 'r')
sys.stdout = open('output3.txt', 'w')

def printSchedule(arr):
    print(len(arr))
    for i in arr:
        print(i[0], i[1])

def calculateMaxCompletedTask(arr):
    newArr = []
    for ind in range(len(arr)):
        min_index = ind
        for j in range(ind + 1, len(arr)):
            if arr[j][1] < arr[min_index][1]:
                min_index = j
        (arr[ind], arr[min_index]) = (arr[min_index], arr[ind])

    newArr.append(arr[0])
    prevStart, prevEnd = arr[0]
    for i in range(1,len(arr)):
        curStart, curEnd = arr[i]
        if curStart >= prevEnd:
            newArr.append(arr[i])
            prevEnd = curEnd

    printSchedule(newArr)


if __name__ == "__main__":
    testCase = int(input())
    data = []
    for _ in range(testCase):
        tup = tuple(map(int, input().split(" ")))
        data.append(tup)
    calculateMaxCompletedTask(data)
    