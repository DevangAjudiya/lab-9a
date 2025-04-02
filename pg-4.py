#use of filter
# di=lambda a :  True if a%2==0 else False
# def prime(a):
#     for i in range(2,a):
#         if(a%i==0) and a!=2:
#            return False
#     return True
# ls=[1,2,3,4,5,6,7,8,9,10]
# f=filter(di,ls)
# print(list(f))
# c=filter(prime,ls)
# print(list(c))

# ls=["madam",'python','malayalam',12321]
def pelindrom(st):
    st=str(st)
    l=len(st)
    for i in range(l//2):
        if st[i]!=st[l-i-1]:
            return False
    return True  
ls=["madam",'python','malayalam',12321]
f1=filter(pelindrom,ls)
print(list(f1))




