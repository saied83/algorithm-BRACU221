import sys
sys.stdin = open('input6.txt', 'r')
sys.stdout = open('output6.txt', 'w')

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def findKthSmallest(arr, low, high, k):
	if k > 0 and k <= high - low + 1:
		pi = partition(arr, low, high)
		if pi - low == k - 1:
			return arr[pi]
		if pi - low > k - 1:
			return findKthSmallest(arr, low, pi - 1, k)
		return findKthSmallest(arr, pi + 1, high,k - pi + low - 1)


def main():
    l = int(input())
    arr = list(map(int, input().split()))
    cases = int(input())
    for i in range(cases):
        result = findKthSmallest(arr, 0, l-1, int(input()))
        print(result)

if __name__ == "__main__":
    main()