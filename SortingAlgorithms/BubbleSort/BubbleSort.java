/**
 * 
 * @author aowang 
 * Date: 08/06/19 
 * Description: Bubble sort algorithm
 *
 */
import java.util.Arrays;

public class BubbleSort {

	public static void main(String[] args) {
		double[] nums = { 1, 9, 2.5, 3, 100, -1.5 };
		bubbleSort(nums);
		print(nums);
		System.out.println(Arrays.toString(nums));
	}

	// The method sorts the array by looping through each element,
	// swapping if the number before it is greater than the current
	// then repeat, but cutting off the end because it is clear
	// that it is the largest
	// i.e. 3,1,5,2

	// first pass
	// step 1: 3 1 5 2 --> 1 3 5 2
	// step 2: 1 3 5 2 --> 1 3 5 2
	// step 3: 1 3 5 2 --> 1 3 2 5

	// second pass
	// step 4: 1 3 2 5 --> 1 3 2 5
	// step 5: 1 3 2 5 --> 1 2 3 5
	// step 6: 1 2 3 5 --> 1 2 3 5

	// third pass (continues to check if all elements are sorted)
	// step 7: 1 2 3 5
	// step 8: 1 2 3 5
	// step 9: 1 2 3 5
	public static void bubbleSort(double[] nums) {

		for (int i = 0; i < nums.length; i++) {
			for (int j = 0; j < nums.length - i - 1; j++) {
				if (nums[j + 1] < nums[j]) {
					swap(nums, j + 1, j);
				}
			}
		}
	}

	// swaps the elements
	public static void swap(double[] nums, int a, int b) {
		double temp = nums[a];
		nums[a] = nums[b];
		nums[b] = temp;
	}

	// prints the array out, however I could import Arrays can use the
	// Arrays.toString()
	public static void print(double[] nums) {
		for (int i = 0; i < nums.length; i++) {
			System.out.print(nums[i] + " ");
		}
		System.out.println();
	}
}
