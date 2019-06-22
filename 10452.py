def main():
    global tc, n, m, grid
    tc = int(input())

    for t in range(tc):
        m, n = map(int, input().split())
        grid = []
        for s in range(m):
            grid += [list(input())]

        dfs(m - 1, grid[m - 1].index('@'))



def dfs(i, j):
    grid[i][j] = 1
    dx = [0, 0, -1]
    dy = [1, -1, 0]
    direc = ['right', 'left', 'forth']

    for k in range(3):
        xc = dx[k] + i
        yc = dy[k] + j

        if valid(xc, yc) and ispath(xc, yc):
            print(direc[k], end=' ')
            dfs(xc, yc)
        elif valid(xc,yc) and grid[xc][yc] == '#':
            print(direc[k])


def valid(i, j):
    return 0 <= i < m and 0 <= j < n


def ispath(i, j):
    return grid[i][j] in 'IEHOVA' if isinstance(grid[i][j], str) else False


main()
