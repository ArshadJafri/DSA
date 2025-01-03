def rev(n, i=1):

    if i >n:
        return
    
    print(i)
    rev(n,i+1)

rev(5)

