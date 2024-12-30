import math

def count(n):

    count =0
    while n > 0:
        n = n//10
        count +=1
    return count


print(count(12112312))



def logic(n):

    return math.log10(n)+1

print(int(logic(123)))