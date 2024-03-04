import sys
sys.stdin = open('input1_A.txt', 'r')
sys.stdout = open('output1_A.txt', 'w')

#only for weighted graph with one edge between two Nodes
def graphRepAdjMatrix():
    (n, m) = tuple(map(int, input().split(" ")))
    graph = [[0]*(n+1) for i in range(n+1)]
    for i in range(m):
        (u, v, w) = tuple(map(int, input().split(" ")))
        graph[u][v] = w
    return graph

def printGraphAdjMatrix(g):
    r = len(g)
    for i in range(r):
        for j in range(r):
            print(g[i][j], end=" ")
        print()
def main():
    graph = graphRepAdjMatrix()
    printGraphAdjMatrix(graph)

if __name__ == "__main__":
    main()


