n = int(input())

tx,ty,tz = 0,0,0
for i in range(n):
    x,y,z = map(int,input().split())
    tx += x
    ty += y
    tz += z

print("YES" if tx == 0 and ty == 0 and tz == 0 else "NO")