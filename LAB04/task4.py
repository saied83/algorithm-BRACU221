import sys

def graphRepAdjList():
    (n, m) = tuple(map(int, input().split(" ")))
    graph = [[] for i in range(n+1)]
    for i in range(m):
        (u, v) = tuple(map(int, input().split(" ")))
        graph[u].append(v)
    return graph


def checkCycleUtil (graph, source, visited, inStack):
    if inStack[source] == 1:
        return True
    if visited[source] == 1:
        return False
    visited[source] = 1
    inStack[source] = 1
    for v in graph[source]:
        if (checkCycleUtil(graph, v, visited, inStack) == True):
            return True
    inStack[source] = -1
    return False


def checkCycle(graph):
    visited = [-1] * len(graph)
    inStack = [0] * len(graph)
    for source in range(len(graph)):
        if (checkCycleUtil(graph, source, visited, inStack) == True):
            return True
    return False


def main():
    sys.stdin = open('input4.txt', 'r')
    sys.stdout = open('output4.txt', 'w')
    g = graphRepAdjList()
    if(checkCycle(g)):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()