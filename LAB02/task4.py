import sys
sys.stdin = open('input4.txt', 'r')
sys.stdout = open('output4.txt', 'w')

def calculateMaxCompletedTask(arr, person):

    for ind in range(len(arr)):
        min_index = ind
        for j in range(ind + 1, len(arr)):
            if arr[j][1] < arr[min_index][1]:
                min_index = j
        (arr[ind], arr[min_index]) = (arr[min_index], arr[ind])

    count = 1
    personArr = [0]*person
    prevEnd = arr[0][1]
    personArr[0] = prevEnd
    
    for i in range(1,len(arr)):
        curStart, curEnd = arr[i]
        for j in range(len(personArr)):
            if personArr[j] <= curStart:
                personArr[j] = curEnd
                count += 1
                break
    print(count)


if __name__ == "__main__":
    testCase, personNumber = tuple(map(int, input().split(" ")))
    data = []
    for _ in range(testCase):
        tup = tuple(map(int, input().split(" ")))
        data.append(tup)
    calculateMaxCompletedTask(data, personNumber)