import sys
from heapq import heappop, heappush

def graphRepAdjList():
    (n, m) = tuple(map(int, input().split(" ")))
    graph = [[] for i in range(n+1)]
    for i in range(m):
        (u, v, w) = tuple(map(int, input().split(" ")))
        graph[u].append((v,w))
    return graph

def find_safest_path(graph, source, destination):
    distance = [float('inf') for node in range(len(graph))]

    distance[source] = 0
    minHeap = [(0, source)]

    while minHeap:
        curDist, curNode = heappop(minHeap)
        if curDist > distance[curNode]:
            continue

        for element, weight in graph[curNode]:
            new_distance = max(curDist, weight)
            if new_distance < distance[element]:
                distance[element] = new_distance
                heappush(minHeap, (new_distance, element))

    if distance[destination] == float('inf'):
        return "Impossible"
    return distance[destination]



def main():
    sys.stdin = open('input3.txt', 'r')
    sys.stdout = open('output3.txt', 'w')
    graph = graphRepAdjList()
    safest_path_distance = find_safest_path(graph, 1, len(graph)-1)
    print(safest_path_distance)


if __name__ == "__main__":
    main()