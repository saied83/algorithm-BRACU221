import sys

def graphRep():
    nodes, m = list(map(int, input().split(" ")))
    graph = []
    for _ in range(m):
        graph.append(list(map(int, input().split(" "))))
    return (nodes,graph)
        
def find(parent, i): 
    if parent[i] != i: 
        parent[i] = find(parent, parent[i]) 
    return parent[i] 


def union(parent, rank, x, y): 
    if rank[x] < rank[y]: 
        parent[x] = y 
    elif rank[x] > rank[y]: 
        parent[y] = x 
    else: 
        parent[y] = x 
        rank[x] += 1

def KruskalMST(nodes, graph): 
    result = [] 
    i = 0
    e = 0
    graph = sorted(graph, key=lambda item: item[2]) 
    parent = [] 
    rank = []

    for node in range(nodes+1): 
        parent.append(node)
        rank.append(0)

    while e < nodes - 1: 
        u, v, w = graph[i] 
        i = i + 1
        x = find(parent, u) 
        y = find(parent, v) 
        if x != y:
            e = e + 1
            result.append([u, v, w]) 
            union(parent, rank, x, y) 

    minimumCost = 0
    for u, v, weight in result: 
        minimumCost += weight  
    print(minimumCost) 

def main():
    sys.stdin = open('input2.txt', 'r')
    sys.stdout = open('output2.txt', 'w')
    n, g = graphRep()
    KruskalMST(n, g)

if __name__ == '__main__': 
	main()


