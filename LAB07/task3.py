import sys

def climb_stairs(n):
    if n <= 1:
        return n
    f = [0] * (n+1)
    f[0] = 1
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

def main():
    sys.stdin = open('input3.txt', 'r')
    sys.stdout = open('output3.txt', 'w')
    n = int(input())
    print(climb_stairs(n))

if __name__ == "__main__":
    main()