def pattern1():
    n = 5
    for i in range(n, 0, -1):
        
        for j in range(i):
            print("*", end="")
        print()
pattern1()
