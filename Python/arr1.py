def func(arr):
    return max(arr), min(arr)


n = 5
arr = list()
for i in range(n):
    arr.append(int(input("Enter")))

print(func(arr))

print("max:", func(arr)[0])
print("max:", func(arr)[1])

# Time complexity : for loop o(n)  func o(n) --> o(n)+o(n) = o(n)