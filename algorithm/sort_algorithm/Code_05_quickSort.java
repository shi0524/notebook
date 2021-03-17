
import java.util.Stack;

public class Code_05_quickSort {

	public static void splitNum(int [] arr){
		int lessEqualR = -1;			// 小与等于区的→边界
		int index = 0;					// 当前下标
		int mostR = arr.length - 1;		// 划分值索引

		while (index < arr.length) {
			if (arr[index] <= arr[mostR]){
				swap(arr, lessEqualR + 1, index);
				lessEqualR++;
				index++;
			}else {
				index++;
			}
		}
	}

	public static void splitNum2(int[] arr){
		int N = arr.length;
		int lessR = -1;					// 小与区域的右边界
		int moreL = N - 1;				// 大于区域的左边界
		int index = 0;					// 当前数索引位置
		// arr[N-1] 划分值
		while (index < moreL){
			if (arr[index] < arr[N-1]){
				// swap(arr, index, lessR+1);
				// lessR++;
				// index++;
				swap(arr, index++, ++lessR);
			}else if (arr[index] == arr[N-1]){
				index++;
			}else{	
				// swap(arr, index, moreL-1);
				// moreL--;
				swap(arr, index, --moreL);
			}
		}
		swap(arr, moreL, N-1);
	}

	public static void swap(int[]arr, int l, int r){
		int temp = arr[l];
		arr[l] = arr[r];
		arr[r] = temp;
	}

	public static void printArray(int [] arr){
		for (int i=0; i<arr.length; ++i){
			System.out.print(arr[i] + " ");
		}
		System.out.println();
	}


	// 递归版本
	public static void quickSort(int [] arr){
		if (arr == null || arr.length <2){
			return;
		}
		process(arr, 0, arr.length - 1);
	}

	public static void process(int [] arr, int L, int R){
		if (L >= R){
			return;
		}
		int [] p = partition(arr, L, R);
		process(arr, L, p[0]-1);
		process(arr, p[1]+1, R);
	}


	// 分层划分
	public static int[] partition(int [] arr, int L, int R){
		int lessR = L - 1;		// 小于区域的右边界
		int moreL = R;			// 大于区域的左边界
		int index = L;			// 当前位置

		// 开始排序
		while (index < moreL){
			if (arr[index] < arr[R]){
				swap(arr, index++, ++lessR);
			} else if (arr[index] > arr[R]){
				swap(arr, index, --moreL);
			} else {
				index++;
			}
		}
		swap(arr, moreL, R);

		return new int[] {lessR+1, moreL};
	}


	// 迭代版本
	public static class Job{
		int L;
		int R;
		public Job(int left, int right){
			L = left;
			R = right;
		}
	}

	public static void quickSort02(int arr[]){
		if (arr == null || arr.length < 2){
			return;
		}
		Stack<Job> stack = new Stack<>();
		stack.push(new Job(0, arr.length-1));
		while (!stack.isEmpty()){
			Job cur = stack.pop();
			int[] equals = partition(arr, cur.L, cur.R);
			if (equals[0]>cur.L){	// 有 < 区域
				stack.push(new Job(cur.L, equals[0]-1));
			}
			if (equals[1]<cur.R){	// 有 > 区域
				stack.push(new Job(equals[1]+1, cur.R));
			}
		}
	}


	public static void main(String [] args){
		int arr1[] = {1, 3, 2, 8, 6, 7, 6, 9, 6, 9, 4, 5, 2, 7, 8, 6};
		int arr2[] = {1, 3, 2, 8, 6, 7, 6, 9, 6, 9, 4, 5, 2, 7, 8, 6};

		printArray(arr1);
		quickSort(arr1);
		quickSort02(arr2);
		printArray(arr1);
		printArray(arr2);
	}

}