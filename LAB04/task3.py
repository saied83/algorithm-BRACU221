import sys
sys.stdin = open('input3.txt', 'r')
sys.stdout = open('output3.txt', 'w')

def graphRepAdjList():
    (n, m) = tuple(map(int, input().split(" ")))
    graph = [[] for i in range(n+1)]
    for i in range(m):
        (u, v) = tuple(map(int, input().split(" ")))
        graph[u].append(v)
    return graph

def DFS():
    pass



def main():
    g = graphRepAdjList()
    DSF(g, 1)

if __name__ == "__main__":
    main()
