/**
 * @author aowang
 * Date: 08/18/19
 * Description: Insertion Sort Algorithm
 */
import java.util.Arrays;

public class Insertion {

	public static void main(String[] args) {
		int[] nums = { 0, -1, 100, 5, -99, 85, 90, 3 };
		System.out.println("Unsorted: " + Arrays.toString(nums));
		insertionSort(nums);
		System.out.println("Sorted: " + Arrays.toString(nums));
	}

	public static void insertionSort(int[] nums) {
		for (int i = 0; i < nums.length; i++) {
			int j = i;
			while (j > 0 && nums[j - 1] > nums[j]) {
				swap(nums, j - 1, j);
				j--;
			}
		}
	}

	public static void swap(int[] nums, int a, int b) {
		int temp = nums[a];
		nums[a] = nums[b];
		nums[b] = temp;
	}

}
