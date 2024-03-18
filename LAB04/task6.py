import sys
sys.stdin = open("input6.txt", 'r')
sys.stdout = open("output6.txt", 'w')


def bfs(graph, r, h, visited):
    row, col = len(graph), len(graph[0])
    diamonds = 0
    Q = [(r, h)]
    visited[r][h] = True
    while Q:
        x, y = Q.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny] and graph[nx][ny] != '#':
                if graph[nx][ny] == 'D':
                    diamonds += 1
                visited[nx][ny] = True
                Q.append((nx, ny))
    return diamonds, visited

def findMaxDiamond(graph, row, col):
    maxDiamonds = 0
    visited = []
    for i in range(row):
        visited.append([False]*col)

    for r in range(row):
        for h in range(col):
            if graph[r][h] == '.':
                d, visited = bfs(graph, r, h, visited)
                maxDiamonds = max(maxDiamonds, d)
    return maxDiamonds


def main():
    row, col = map(int, input().split())
    graph = []
    for i in range(row):
        graph.append(input())
    result = findMaxDiamond(graph, row, col)
    print(result)

if __name__ == "__main__":
    main()