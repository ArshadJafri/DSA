def duplicates(arr):

    a =set()
    for num in arr:
        if num in a:
            return True
        a.add(num)

    return False


print(duplicates([1,2,3,1]))