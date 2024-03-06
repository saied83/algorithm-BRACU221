import sys

def graphRepAdjList():
    (n, m) = tuple(map(int, input().split(" ")))
    graph = [[] for i in range(n+1)]
    for i in range(m):
        (u, v) = tuple(map(int, input().split(" ")))
        graph[u].append(v)
        graph[v].append(u)
    return graph


def DFS(graph, source):
    visited = [-1]*len(graph)
    # sequence = str(source) + " "
    sequence = ""
    visited[source] = 0

    # for i in range(len(graph[source])):
    #     u = graph[source][i]
    #     if visited[u] == -1:
    #         (visited, sequence) = DFSvisit(graph, u, visited, sequence)
    (visited, sequence) = DFSvisit(graph, source, visited, sequence)
    print(sequence)

def DFSvisit(graph, u, visited, sequence):
    visited[u] = 1
    sequence = sequence + str(u) + " "
    for i in range(len(graph[u])):
        element = graph[u][i]
        if visited[element] == -1:
            (visited, sequence) = DFSvisit(graph, element, visited, sequence)

    return (visited, sequence)


def main():
    sys.stdin = open('input3.txt', 'r')
    sys.stdout = open('output3.txt', 'w')
    g = graphRepAdjList()
    DFS(g, 1)


if __name__ == "__main__":
    main()
