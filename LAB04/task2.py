import sys

def graphRepAdjList():
    (n, m) = tuple(map(int, input().split(" ")))
    graph = [[] for i in range(n+1)]
    for i in range(m):
        (u, v) = tuple(map(int, input().split(" ")))
        graph[u].append(v)
        graph[v].append(u)
    return graph

def BSF(graph, source):
    visited = [-1]*len(graph)
    Q = []
    sequence = str(source)
    Q.append(source)
    while len(Q) != 0:
        s = Q.pop(0)
        Adj = graph[s]
        for i in range(len(Adj)):
            element = Adj[i]
            if visited[element] == -1:
                visited[element] = 0
                # parent[element] = s
                # level[element] = level[s] +1
                sequence += " " + str(element)
                Q.append(element)
        visited[s] = 1

    print(sequence)



def main():
    sys.stdin = open('input2.txt', 'r')
    sys.stdout = open('output2.txt', 'w')
    g = graphRepAdjList()
    BSF(g, 1)

if __name__ == "__main__":
    main()
