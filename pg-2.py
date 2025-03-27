a=lambda a: a**3
ls=[1,2,3,4,5,6,7,8,9,10]
m=map(a,ls)
print(list(m))
ls1=[1,2,3,4,5,6]
ls2=[6,5,4,3,2,1]
add = lambda a,b : a+b
m=map(add,ls1,ls2)
print(list(m))
