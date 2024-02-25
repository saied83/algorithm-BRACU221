import sys
sys.stdin = open('input1.txt', 'r')
sys.stdout = open('output1.txt', 'w')

def printResult(arr):
    for indx in range(len(arr)):
        print(arr[indx], end=" ")
        
def merge(a, b):
    final_list = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            final_list.append(a[i])
            i += 1
            continue
        final_list.append(b[j])
        j += 1
    while i < len(a):
        final_list.append(a[i])
        i = i + 1
    while j < len(b):
        final_list.append(b[j])
        j = j + 1
        
    return final_list  

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = merge_sort(arr[0:mid])
        a2 = merge_sort(arr[mid:])
        return merge(a1, a2)

def main():
    testCase = int(input())
    arr = list(map(int, input().split(" ")))
    printResult(merge_sort(arr))

if __name__ == "__main__":
    arr = [9,5,4,6,1,3,2,9]
    printResult(merge_sort(arr))
    

