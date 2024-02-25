import sys
sys.stdin = open('input2.txt', 'r')
sys.stdout = open('output2.txt', 'w')

def findMax(left, right):
    if left > right:
        return left
    else:
        return right

def divideAndFindMax(arr):
    if len(arr) == 1:
        return arr[0]
    mid = len(arr)//2
    left = divideAndFindMax(arr[:mid])
    right = divideAndFindMax(arr[mid:])
    return findMax(left, right)

def main():
    testCase = int(input())
    arr = list(map(int, input().split(" ")))
    result = divideAndFindMax(arr)
    print(result)

if __name__ == "__main__":
    main()
    
# Time Complexity of this code
# T(n) = 2*T(n/2) + O(1)