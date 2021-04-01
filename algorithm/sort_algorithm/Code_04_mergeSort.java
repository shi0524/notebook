public class Code_04_mergeSort {

	// 递归版本实现
	public static void mergeSort01(int[] arr){
		if (arr == null || arr.length<2){
			return;
		}
		process(arr, 0, arr.length-1);
	}

	public static void process(int[] arr, int L, int R){
		// base case
		if (L == R){
			return;
		}
		int mid = L + ((R - L) >> 1);
		process(arr, L, mid);
		process(arr, mid+1, R);
		merge(arr, L, mid, R);
	}

	public static void merge(int[] arr, int L, int M, int R){
		int[] help = new int[R - L + 1];
		int i = 0;
		int p1 = L;
		int p2 = M + 1;
		while (p1 <= M && p2 <= R){
			help[i++] = arr[p1] <= arr[p2] ? arr[p1++] : arr[p2++];
		}
		while (p1 <= M){
			help[i++] = arr[p1++];
		}

		while (p2 <= M){
			help[i++] = arr[p2++];
		}

		for (i=0; i < help.length; ++i){
			arr[L+i] = help[i];
		}
	}

}