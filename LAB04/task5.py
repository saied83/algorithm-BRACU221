import sys

def graphRepAdjList():
    (n, m, d) = tuple(map(int, input().split(" ")))
    graph = [[] for i in range(n+1)]
    for i in range(m):
        (u, v) = tuple(map(int, input().split(" ")))
        graph[u].append(v)
        graph[v].append(u)
    return graph, d

def BFS(graph, source, parent, distance):
    q = []
    distance[source] = 0
    q.append(source)

    while len(q) != 0:
        source = q.pop(0)
        for element in graph[source]:
            if distance[element] == float('inf'):
                parent[element] = source
                distance[element] = distance[source] + 1
                q.append(element)


def findShortDistance(graph, source, destination):
    parent = [-1] * len(graph)
    distance = [float('inf')] * len(graph)
    BFS(graph, source, parent, distance)

    if distance[destination] == float('inf'):
        print("Source and Destination are not connected")
        return

    print("Time:",distance[destination])

    path = []
    curNode = destination
    path.append(destination)
    while parent[curNode] != -1:
        path.append(parent[curNode])
        curNode = parent[curNode]
    print("Shortest Path:", end=" ")
    for i in range(len(path) - 1, -1, -1):
        print(path[i], end=" ")


def main():
    sys.stdin = open('input5.txt', 'r')
    sys.stdout = open('output5.txt', 'w')
    graph, destination = graphRepAdjList()
    findShortDistance(graph, 1, destination)

if __name__ == "__main__":
    main()
