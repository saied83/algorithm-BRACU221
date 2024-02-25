import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

# Two pointers
# it runs in 0(k*N)
def swapBlackTilesNk(l, arr, k):
    pointer1, pointer2 = 0, k-1
    min = k
    while pointer2 < l:
        count = 0
        for i in range(k):
            if arr[pointer1+i] == 1:
                count += 1
        if count < min:
            min = count
        pointer1 +=1
        pointer2 +=1
    return min

# Two pointers
# it runs in 0(N)
def swapBlackTilesN(l, arr, k):
    p1 = count = 0
    for i in range(k):
        if arr[i] == 1:
            count += 1
    min = count
    p2 = k-1
    while p2+1 < l:
        p2+=1
        if arr[p2] == 0 and arr[p1] == 1:
            count -= 1
        elif arr[p2] == 1 and arr[p1] == 0:
            count +=1
        if count < min:
            min = count
        p1 +=1
    return min


if __name__ == "__main__":
    len = int(input())
    arr = []
    for i in input():
        arr.append(int(i))
    # arr = list(map(int, input().split(" ")))
    k = int(input())
    result = swapBlackTilesN(len, arr, k)
    print(result)
    result = swapBlackTilesN2(len, arr, k)
    print(result)
