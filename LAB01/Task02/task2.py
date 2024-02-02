import sys
sys.stdin = open("./input2.txt", 'r')
sys.stdout = open("./output2.txt", 'w')

def bubbleSort(arr):

    isSorted = True
    for i in range(len(arr)-1):
        if arr[i]>=arr[i+1]:
            isSorted = False
            break
    if isSorted:
        return arr
    else:
        for i in range(len(arr)-1):
            for j in range(len(arr)-i-1): 
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

if __name__ == "__main__":
    lenOfArr = int(input())
    arr = list(map(int, input().split()))
    resultArr = bubbleSort(arr)
    print(resultArr)
