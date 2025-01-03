def rev_arr(arr):
    if len(arr) == 0:
        return
    print(arr[-1])
    rev_arr(arr[:-1])

rev_arr([1,2,3,4,5])