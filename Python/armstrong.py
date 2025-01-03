def armstrong(n):

    count = 0
    real = n
    rea =n
    arm =0
    while n>0:
        n =n//10
        count +=1
    print(count)
    while real >0:
        s =real%10
        arm  += s**count
        real = real//10
    print(arm)
    print(rea)
    
    if rea == arm:
        return True
    else:
        return False


print(armstrong(153)) 
    