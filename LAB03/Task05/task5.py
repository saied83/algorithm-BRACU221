import sys
sys.stdin = open('input5.txt', 'r')
sys.stdout = open('output5.txt', 'w')

def partition(array, low, high):

	pivot = array[high]
	i = low - 1
	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1
			array[i], array[j] = array[j], array[i]
	array[i + 1], array[high] = array[high], array[i + 1]
	return i + 1

def quickSort(array, low, high):
	if low < high:
		p = partition(array, low, high)
		quickSort(array, low, p - 1)
		quickSort(array, p + 1, high)

def printArr(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
def main():
    l = int(input())
    arr = list(map(int, input().split(" ")))
    quickSort(arr, 0, l-1)
    printArr(arr)

if __name__ == "__main__":
    main()
