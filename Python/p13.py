def pattern():
    n = 5
    k = 1
    for i in range(n):
        for j in range(i+1):
            print(j+1,end=" ")
            k +=1
        print()

pattern()