// File: DSA.java
import java.util.Scanner;

public class DSA {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Take input from the user
        System.out.println("Enter the size of array:");
        int n = sc.nextInt();

        System.out.println("Enter the target value:");
        int target = sc.nextInt();

        int[] arr = new int[n];
        System.out.println("Enter the values:");

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        // Call the binarySearch method from BinarySearch class
        int result = BinartSearch.binarySearch(arr, target);

        // Output the result
        if (result != -1) {
            System.out.println("Element found at index: " + result);
        } else {
            System.out.println("Element not found.");
        }

        sc.close();
    }
}
