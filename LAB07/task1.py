import sys

def find(parent, node):
    while parent[node] != node:
        node = parent[node]
    return parent[node]

def printSetNodes(parent, node):
    count = 0
    for i in parent:
        if i == node:
            count += 1
    print(count)

def union(parent, node1, node2):
    node1Parent = find(parent, node1)
    node2Parent = find(parent, node2)
    for i in range(1,len(parent)):
        if parent[i] == node2Parent:
            parent[i] = node1Parent
    printSetNodes(parent, node1Parent)

def disjoint(nodes, connection):
    parent = []
    for i in range(nodes+1):
        parent.append(i)
    for i in range(connection):
        node1, node2 = list(map(int, input().split(" ")))
        union(parent, node1, node2)


def main():
    sys.stdin = open('input1.txt', 'r')
    sys.stdout = open('output1.txt', 'w')
    nodes, connection = list(map(int, input().split(" ")))
    disjoint(nodes, connection)

if __name__ == "__main__":
    main()