import math as Math
def divisors(n):

    div =[]

    for i in range(1,n+1):
        if n%i==0:
            div.append(i)

    return div

print(divisors(12))

def mod(n):

    div =[]

    for i in range(1, int(Math.sqrt(n)+1)):
        if n%i==0:
            div.append(i)

    return div

print(mod(36))