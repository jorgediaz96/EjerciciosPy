from functools import reduce
l=[16,22,44,23]
p=list(map(lambda x:list(str(x)),l))
n=list(filter(lambda j: reduce(lambda x,y: int(x)%2==0 and int(y)%2==0,j),p))
n=list(map(lambda a:reduce(lambda c,b:c+b,a),n))
n=list(map(lambda a:int(a),n))
print(n)
