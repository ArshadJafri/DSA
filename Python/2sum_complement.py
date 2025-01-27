def complement(arr,target):

    hash_map ={}

    for i in range(len(arr)):
        complement = target- arr[i]

        if complement in hash_map:
            print("this ",hash_map[complement],i)
            return (hash_map[complement],i)

        hash_map[arr[i]] = i
        print(hash_map)
        
    
    return [-1,-1]


print(complement([11,2,15,7],9))