import sys
sys.stdin = open('input4.txt', 'r')
sys.stdout = open('output4.txt', 'w')

def merge(arr, left, mid, right):

    arr1 = arr[left:mid]
    arr2 = arr[mid:right + 1]
    i = 0
    j = 0
    k = left
    maxVal = float('-inf')

    while i < len(arr1) and j < len(arr2):
        if arr1[i] + arr2[j] ** 2 > maxVal:
            maxVal = arr1[i] + arr2[j] ** 2
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1

    return maxVal


def mergeSort(arr, left, right):
    maxVal = float('-inf')
    if left < right:
        mid = (left + right) // 2
        maxVal = max(maxVal, mergeSort(arr, left, mid))
        maxVal = max(maxVal, mergeSort(arr, mid + 1, right))
        maxVal = max(maxVal, merge(arr, left, mid, right))
    return maxVal

def main():
    l = int(input())
    arr = list(map(int, input().split(" ")))
    maxVal = mergeSort(arr, 0, len(arr)-1)
    print(maxVal)

if __name__ == "__main__":
    main()