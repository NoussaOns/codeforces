def main():
    tc = 0
    while 1:
        try:
            global n
            n = int(input())
            global grid
            grid = []
            global seen
            seen = [[0] * n] * n
            ans = 0
            for i in range(n):
                grid += [list(input())]

            for i in range(n):
                for j in range(n):
                    if not seen[i][j] and grid[i][j] == '1':
                        dfs(i, j)
                        ans += 1
            tc += 1
            print("Image number %d contains %d war eagles." %(tc,ans))
        except EOFError:
            break


def valid(i, j):
    return i >= 0 and j >= 0 and i < n and j < n


def dfs(i, j):
    if seen[i][j]:
        return

    seen[i][j] = 1
    print(seen)


    dx = [0, 0, 1, 1, 1, -1, -1, -1]
    dy = [1, -1, 1, 0, -1, 1, 0, -1]

    for k in range(8):
        xc = dx[k] + i
        yc = dy[k] + j

        if valid(xc, yc) and not seen[xc][yc] and grid[xc][yc] == '1':
            dfs(xc, yc)


main()
