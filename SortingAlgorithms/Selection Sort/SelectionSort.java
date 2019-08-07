/**
 * 
 * @author aowang
 * Date: 08/07/19
 * Description: Simple selection sort algorithm
 *
 */
import java.util.Arrays;

public class SelectionSort {

	public static void main(String[] args) {
		double[] nums = { -1, 99, 0, 5, 25, 100 };
		selectionSort(nums);
		print(nums);
		System.out.println(Arrays.toString(nums));

	}

	// The sorting algorithm finds the smallest element in the array
	// then swaps it in the first index position, then repeats the process,
	// but placing the next smallest in the earlier indexes

	// i.e. [-1, 99, 0, 5, 25, 100]
	// first: [-1, 99, 0, 5, 25, 100] --> [-1, 99, 0, 5, 25, 100] -1 is the
	// smallest, no swap
	// second: [-1, 99, 0, 5, 25, 100] --> [-1, 0, 99, 5, 25, 100] swaps 0 to the
	// 99's index
	// third: [-1, 0, 99, 5, 25, 100] --> [-1, 0, 5, 99, 25, 100]
	// fourth: [-1, 0, 5, 99, 25, 100] --> [-1, 0, 5, 25, 99, 100]
	// fifth: [-1, 0, 5, 25, 99, 100] -- > [-1, 0, 5, 25, 99, 100]

	public static void selectionSort(double[] nums) {
		for (int i = 0; i < nums.length - 1; i++) {
			int min = i;

			// similar algorithm to find smallest number
			for (int j = i + 1; j < nums.length; j++) {
				if (nums[j] < nums[min]) {
					min = j;
				}
			}
			swap(nums, min, i);
		}
	}

	// The method swaps two numbers in the array
	public static void swap(double[] nums, int a, int b) {
		double temp = nums[a];
		nums[a] = nums[b];
		nums[b] = temp;
	}

	// prints the array out
	public static void print(double[] nums) {
		for (int i = 0; i < nums.length; i++) {
			System.out.print(nums[i] + " ");
		}
		System.out.println();
	}
}
