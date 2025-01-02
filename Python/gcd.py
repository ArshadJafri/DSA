def gcd(n,m):

    gcd = 1

    for i in range(1,min(n,m)+1):
        if n%i==0 and m%i==0:
            gcd =i
        
    return gcd

print(gcd(12,14))

def bgcd(n,m):

    while n !=0 and m!=0:
        if n>m:
            n=n-m
        else:
            m=m-n
    
    return (max(n,m))

print("Printthis",bgcd(12,14))