def insertion(arr):
    
    n = len(arr)
    for i in range(1,n):
        j = i-1

        while(j>=0 and arr[j] >arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
            j -=1
        
    return arr 

print(insertion([64,34,25,12,22,11,90]))