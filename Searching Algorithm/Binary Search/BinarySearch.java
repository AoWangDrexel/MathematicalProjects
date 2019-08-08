
/**
 * @author aowang
 * Date: 08/08/19
 * Description: Simple binary search algoritm
 */

import java.util.Arrays;

public class BinarySearch {

	public static void main(String[] args) {
		int[] nums = { -1, 0, -99, 200, 95, 5 };
		System.out.println(Arrays.toString(nums));

		// in order for the binary search to work, the array has to be sorted
		Arrays.sort(nums);

		int find = 200;
		System.out.println(Arrays.toString(nums));
		System.out.println(find + " can be found at index: " + binarySearch(nums, find));
	}

	// The method first goes to the middle of the index
	// checks if the number wanted is less than or greater
	// than it. If it is, cut off the half that is either greater
	// or less than and repeat

	// i.e. 1 2 3 4 5 find 4
	// low is 0, high is 4, mid is 2
	// nums[mid] is 3, 3 < 4? yes so low is now mid + 1
	// 4 5 is now checked, repeat the process till it returns 3
	public static int binarySearch(int[] nums, int find) {
		int low = 0;
		int high = nums.length - 1;
		while (low <= high) {
			int mid = (low + high) / 2;
			if (nums[mid] < find) {
				low = mid + 1;
			} else if (nums[mid] == find) {
				return mid;
			} else {
				high = mid - 1;
			}
		}
		return -1;
	}
}

