def lenth(st):
    st=str(st)
    l=len(st)
    if l>8:
        return True
    return False  
ls=["madam",'python','malayalam',12321]
f1=filter(lenth,ls)
print(list(f1))
