n = 5  # Number of rows

for i in range(1, n + 1):
    # Print increasing numbers
    for j in range(1, i + 1):
        print(j, end="")
    
    # Print spaces
    for _ in range(2 * (n - i)):
        print(" ", end="")
    
    # Print decreasing numbers
    for j in range(i, 0, -1):
        print(j, end="")
    
    # Move to the next line
    print()
