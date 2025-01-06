def selection(arr):
    n= len(arr)
    for i in range(n-1):
        min_index = i 
        for j in range(i+1, n):
            if arr[j] <arr[min_index]:
                min_index = j
        
        if arr[min_index] !=arr[i]:
            arr[min_index],arr[i] = arr[i],arr[min_index]

    return arr

arr = [64, 25, 12, 22, 11]
print(selection(arr))