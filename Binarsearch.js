function binarySearch(arr, target) {
    let left = 0;
    let right = arr.length - 1;

    while (left <= right) {
        let mid = Math.floor((left + right) / 2); // correct midpoint calculation

        if (arr[mid] === target) {
            console.log("Found target at index =", mid);
            return mid; // return or break after finding
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    console.log("Target not found in array");
    return -1;
}

binarySearch([10, 20, 30, 40], 20);
