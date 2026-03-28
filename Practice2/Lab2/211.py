n, l, r = map(int, input().split())
a=list(map(int,input().split()))
sub=a[l-1:r] 
sub.reverse()
a[l-1:r] = sub
for x in a: 
    print(x , end=" ") 