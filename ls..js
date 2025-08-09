// your code goes here


function linearSearch(arr, target) {
    
    for(let i =0; i< arr.length; i++){
        
        if(arr[i]== target){
            return i;
            break;
        }
    }
    return -1;
}

const res = linearSearch([10,20,30], 20)


if(res == -1){
    console.log("The target is not in the array")
}

else{
    
    console.log("The target is found at position",res+1)
}
