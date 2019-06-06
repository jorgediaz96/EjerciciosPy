from functools import reduce
l=[[16,22,44,23],[10,20,40,50]]
e=lambda x:list(str(x))
e=list(map(lambda a:list(map(t,a)),e))
e=list(map(lambda a:list(filter(lambda h:reduce(lambda j,n:int(j)%2==0 and int(n)%2==0),a)),e))
e=list(filter(lambda a:a!=[],e))
e=list(map(lambda a:list(map(lambda h:reduce(lambda j,n:j+n,h),a)),e))
e=list(map(lambda a:list(map(lambda v:int(v),a)),e))
e=list(map(lambda y:reduce(lambda a,b:a if a<b else b,y),e))
print(e)
