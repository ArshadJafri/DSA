// File: BinarySearch.java
public class BinartSearch {

    // Static method for Binary Search
    public static int binarySearch(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;  // Calculate mid index

            if (arr[mid] == target) {
                return mid;  // Target found at index 'mid'
            } else if (arr[mid] < target) {
                left = mid + 1;  // Search in the right half
            } else {
                right = mid - 1;  // Search in the left half
            }
        }
        
        return -1;  // Element not found
    }
}
