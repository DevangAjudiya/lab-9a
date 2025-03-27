import random
ls=[]
for i in range(10):
    a=random.randint(-15,15)
    ls.append(a)
print(ls)
sqr= lambda a :a**2
print(list(map(sqr,ls)))
