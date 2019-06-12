n,k = map(int,input().split())

a = list(map(int, input().split()))
print(len(a) - a.count(0) if (a[k-1] <= 0) else (a.count(a[k-1])+a.index(a[k-1])))