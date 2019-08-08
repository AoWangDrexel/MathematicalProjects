/**
 * @author aowang
 * Date: 08/08/19
 * Description: You probably already know this: Simple linear search algorithm
 */

import java.util.Arrays;

public class LinearSearch {

	public static void main(String[] args) {
		int[] nums = { -1, 0, -99, 200, 95, 5 };
		System.out.println(Arrays.toString(nums));
		
		int find = -99;
		System.out.println(find + " can be found at index: " + linearSearch(nums, find));

	}
	
	// The method goes through each element and returns the index,
	// if not found, return -1
	public static int linearSearch(int[] nums, int find) {
		for (int i = 0; i < nums.length; i++) {
			if (nums[i] == find) {
				return i;
			}
		}
		return -1;
	}
}

