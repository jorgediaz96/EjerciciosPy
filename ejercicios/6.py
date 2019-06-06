from functools import reduce
l=[(6,3),(15,5),(8,9)]
m=list(map(lambda x:x[0] if x[0] == (x[1]*(x[1]+1)/2) else 0,l))
tri=reduce(lambda a,b:a+b,m)
print(tri)
