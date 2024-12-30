def palindrom(n):

    rev = 0
    temp = n



    while n > 0:
        l = n % 10
        rev = rev *10 +l
        n = n//10


    if temp == rev:
        return True 
    else:
        return False

print(palindrom(12))