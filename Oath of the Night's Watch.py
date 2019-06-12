n = input()

a= list(map(int,input().split()))

ma = max(a)
mi = min(a)

maxs = a.count(ma)
mins = a.count(mi)
res = len(a) - maxs - mins
print(res if res > 0 else 0)