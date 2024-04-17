import sys

def graphRepAdjList():
    (n, m) = tuple(map(int, input().split(" ")))
    graph = [[] for i in range(n+1)]
    inDeg = [0]*(n+1)
    for i in range(m):
        (u, v) = tuple(map(int, input().split(" ")))
        graph[u].append(v)
        inDeg[v] +=1
    return (graph, inDeg, n)

def bfs(G, v, visited, result, Q, inDeg):
    visited.append(v)
    Q.append(v)
    while Q:
        x = Q.pop(0)
        result.append(x)
        for adj in G[x]:
            inDeg[adj] -= 1
            if adj not in visited and inDeg[adj] == 0:
                visited.append(adj)
                Q.append(adj)

def topSort(graph, inDeg, node):
    result = []
    visited = []
    Q = []
    for i in range(1,len(graph)):
        if inDeg[i] == 0 and i not in visited:
            bfs(graph, i, visited, result, Q, inDeg)

    if len(result) < node:
        print('IMPOSSIBLE')
    else:
        for i in result:
            print(i, end=" ")

def main():
    sys.stdin = open('input1_B.txt', 'r')
    sys.stdout = open('output1_B.txt', 'w')
    graph, inDeg, node = graphRepAdjList()
    topSort(graph, inDeg, node)

if __name__ == "__main__":
    main()