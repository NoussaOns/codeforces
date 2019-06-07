while(1):
    n = int(input())
    if n == 0:
        break

    totd = 0
    totc = 0
    for i in range(n):
        leap = False
        d,m,y,c = map(int,input().split())
        if i == 0:
            tm = m
            ty = y
            td = d
            tc = c
        if (y % 4 == 0 and y % 100 != 0):
            leap = True

        nd = 31 if (tm <= 7 and tm % 2 == 1) or (tm >= 8 and tm % 2 == 0) else 30
        if tm == 2 and not leap:
            nd = 28
        elif tm == 2 and leap:
            nd = 29

        if (y == ty and m == tm and d - td == 1) or (y == ty and m - tm == 1 and td == nd and d == 1) or (y - ty == 1 and tm == 12 and td == 31 and m==1 and d == 1):
            totd +=1
            totc += c - tc

        td,tm,ty,tc = d,m,y,c

    print(totd, totc)