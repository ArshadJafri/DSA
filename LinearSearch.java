
import java.util.Scanner;
public class DSA {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		System.out.println("This is the Main Page");
		
		int target = sc.nextInt();
		
		
		System.out.println("Enter the number of values");
		int n = sc.nextInt();
		int nums[] = new int[n];
		
		System.out.println("Enter the values");
		for(int i =0; i<n; i++) {
			nums[i] = sc.nextInt();
		}
		
		int linear = LinearSearch(nums, target);
		if(linear ==1) {
			System.out.println("Element found");
		}else {
			System.out.println("Element not found");
			
		}
			

	}

	public static int LinearSearch(int[] nums, int target) {
		// TODO Auto-generated method stub
		
		for(int i=0; i<nums.length; i++) {
			if(nums[i] == target) {
				return 1;
			}
		}
		return -1;
		
	}

	

}
