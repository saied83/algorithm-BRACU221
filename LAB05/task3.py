import sys

def graphRepAdjList():
    (n, m) = tuple(map(int, input().split(" ")))
    graph = [[] for i in range(n+1)]
    revGraph = [[] for i in range(n+1)]
    for i in range(m):
        (u, v) = tuple(map(int, input().split(" ")))
        graph[u].append(v)
        revGraph[v].append(u)
    return (graph, revGraph)


def dfs(G, v, visited, stack, revTraversal=True, compList = None):
    visited.append(v)
    if not revTraversal:
        compList.append(v)
    for element in G[v]:
        if element not in visited:
            dfs(G, element, visited,stack, revTraversal, compList)
    if revTraversal:
        stack.append(v)


def ssComponent(graph, revGraph):
    result = []
    visited = []
    stack = []
    for i in range(1,len(graph)):
        if i not in visited:
            dfs(graph, i, visited, stack)

    visited = []
    components = []
    while stack:
        l = []
        x = stack.pop()
        if x not in visited:
            dfs(revGraph,x,visited,stack, revTraversal=False, compList=l)

        if l:
            components.append(l)
        
    for i in components:
        if len(i) > 0:
            for j in i:
                print(j, end=" ")
        print()


def main():
    sys.stdin = open('input3.txt', 'r')
    sys.stdout = open('output3.txt', 'w')
    graph, revGraph = graphRepAdjList()
    ssComponent(graph, revGraph)

if __name__ == "__main__":
    main()
