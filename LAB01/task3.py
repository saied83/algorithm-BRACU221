import sys
sys.stdin = open('input3.txt', 'r')
sys.stdout = open('output3.txt', 'w')

def selectionSort(arr):
    for i in range(len(arr)):
        min_indx = i
        for j in range(i+1, len(arr)):
            if arr[min_indx] > arr[j]:
                min_indx = j
        arr[min_indx], arr[i] = arr[i], arr[min_indx]
    return arr

def uniqueNumbers(arr):
    newArr = []
    for i in range(len(arr)):
        if arr[i] not in newArr:
            newArr.append(arr[i])
    return newArr
def rankStudents(N, ids, marks):
    data = {}
    for i in range(N):
        id = ids[i]
        mark = marks[i]
        if mark not in data.keys():
            data[mark] = [id]
        else:
            data[mark].append(id)

    updatedMarks = uniqueNumbers(marks)
    sortedMarks = selectionSort(updatedMarks)
    desecdingSortedMarks = sortedMarks[::-1]

    for x,y in data.items():
        data[x] = selectionSort(y)


    for i in desecdingSortedMarks:
        for j in data[i]:
            print(f'ID: {j} Mark: {i}')


if __name__ == "__main__":
    N = int(input())
    ids = list(map(int, input().split(" ")))
    marks = list(map(int, input().split(" ")))
    rankStudents(N, ids, marks)