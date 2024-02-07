import sys
sys.stdin = open('input2.txt', 'r')
sys.stdout = open('output2.txt', 'w')

def sortMergeArrayType1(arr1, arr2):
    newArr = arr1 + arr2
    newArr.sort()
    return newArr

def sortMergeArrayType2(len1, len2, arr1, arr2):
    newArray = [None]*(len1+len2)
    pointer1 = 0
    pointer2 = 0
    i = 0
    while pointer1<len1 and pointer2<len2:
        if arr1[pointer1] < arr2[pointer2]:
            newArray[i] = arr1[pointer1]
            pointer1 += 1
            i += 1
        elif arr1[pointer1] > arr2[pointer2]:
            newArray[i] = arr2[pointer2]
            pointer2 += 1
            i += 1

    if pointer1 < len1:
        newArray[i:] = arr1[pointer1:]
    elif pointer2 < len2:
        newArray[i:] = arr2[pointer2:]
    return newArray


if __name__ == "__main__":
    len1 = int(input())
    arr1 = list(map(int, input().split(" ")))
    len2 = int(input())
    arr2 = list(map(int, input().split(" ")))
    resultArray1 = sortMergeArrayType1(arr1, arr2)
    resultArray2 = sortMergeArrayType2(len1, len2, arr1, arr2)
    print(resultArray1)
    print(resultArray2)
