import java.util.Arrays;

public class MergeSort {

	public static void main(String[] args) {

		int[] nums = { 0, -1, 100, 5, -99, 85, 90, 3 };
		System.out.println("Unsorted: " + Arrays.toString(nums));
		System.out.println("Sorted: " + Arrays.toString(mergeSort(nums)));
	}

	public static int[] mergeSort(int[] nums) {

		if (nums.length == 1) {
			return nums;
		}

		int mid = nums.length / 2;
		int[] left = new int[mid];
		int[] right = new int[nums.length - mid];

		for (int i = 0; i < left.length; i++) {
			left[i] = nums[i];
		}
		for (int i = 0; i < right.length; i++) {
			right[i] = nums[mid + i];
		}

		left = mergeSort(left);
		right = mergeSort(right);

		return merge(left, right);

	}

	public static int[] merge(int[] left, int[] right) {

		int[] result = new int[left.length + right.length];

		int leftInd = 0;
		int rightInd = 0;
		int resultInd = 0;

		while (leftInd < left.length || rightInd < right.length) {
			if (leftInd < left.length && rightInd < right.length) {
				if (left[leftInd] < right[rightInd]) {
					result[resultInd++] = left[leftInd++];
				} else {
					result[resultInd++] = right[rightInd++];
				}
			} else if (leftInd < left.length) {
				result[resultInd++] = left[leftInd++];
			} else if (rightInd < right.length) {
				result[resultInd++] = right[rightInd++];
			}
		}

		return result;
	}
}

