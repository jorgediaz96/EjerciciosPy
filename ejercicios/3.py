from functools import reduce
l = [(5,4,5,6),(3,2,5,6),(2,4,6,8),(6,7,7,6)]
m=list(map(lambda y:reduce(lambda x,z:x if x>z else z,y),l))
print(m) 
