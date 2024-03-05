import sys

def graphRepAdjList():
    (n, m) = tuple(map(int, input().split(" ")))
    graph = [[] for i in range(n+1)]
    for i in range(m):
        (u, v, w) = tuple(map(int, input().split(" ")))
        graph[u].append((v,w))

    return graph

def printGraphAdjList(g):
    for i in range(len(g)):
        print(i,":",end=" ")
        for j in range(len(g[i])):
            print(g[i][j], end=" ")
        print()
        
def main():
    sys.stdin = open('input1_B.txt', 'r')
    sys.stdout = open('output1_B.txt', 'w')
    g = graphRepAdjList()
    printGraphAdjList(g)

if __name__ == "__main__":
    main()
