import sys
import heapq

def graphRepAdjList():
    (n, m) = tuple(map(int, input().split(" ")))
    graph = [[] for i in range(n+1)]
    inDeg = [0]*(n+1)
    for i in range(m):
        (u, v) = tuple(map(int, input().split(" ")))
        graph[u].append(v)
        inDeg[v] +=1
    return (graph, inDeg, n)

def bfs(graph, v, visited, result, pQ, inDeg):
    visited.append(v)
    heapq.heappush(pQ,v)
    while pQ:
        x = heapq.heappop(pQ)
        result.append(x)
        for element in graph[x]:
            inDeg[element] -= 1
            if element not in visited and inDeg[element] == 0:
                visited.append(element)
                heapq.heappush(pQ,element)

def topSort(graph, inDeg, node):
    result = []
    visited = []
    pQ = []
    heapq.heapify(pQ)
    for i in range(1,len(graph)):
        if inDeg[i] == 0 and i not in visited:
            bfs(graph, i, visited, result, pQ, inDeg)

    if len(result) < node:
        print('IMPOSSIBLE')
    else:
        for i in result:
            print(i, end=" ")

def main():
    sys.stdin = open('input2.txt', 'r')
    sys.stdout = open('output2.txt', 'w')
    graph, inDeg, node = graphRepAdjList()
    topSort(graph, inDeg, node)

if __name__ == "__main__":
    main()