l = [[5,4,5,6],[3,2,5,6],[2,4,6,8],[6,7,7,6]]
m=list(map(lambda x:[x[0]]+[x[len(x)-1]],l))
print(m)
