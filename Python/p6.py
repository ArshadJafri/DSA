def pattern1():
    n = 5
    for i in range(n, 0, -1):
        
        for j in range(i):
            print(j+1, end="")
        print()
pattern1()
