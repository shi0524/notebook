
/**
* 选择排序
**/
import java.util.Arrays;

public class Code_01_selectionSort{

	public static void swap(int[] arr, int idex1, int idex2){
		int temp = arr[idex1];
		arr[idex1] = arr[idex2];
		arr[idex2] = temp;
	}

	public static void selectSort(int [] arr){
		if (null == arr || arr.length < 2){
			return;
		}
		int N  = arr.length;
		for (int i=0; i<N; ++i){
			int min_index = i;
			for (int j=i+1; j<N; ++j){
				if (arr[min_index] > arr[j])
					swap(arr, min_index, j);
			}
		}
	}


	public static void main(String [] args){
		int [] arr = {1,4,7,3,9, 11, 45,2,4};
		System.out.println(Arrays.toString(arr));
		selectSort(arr);
		System.out.println(Arrays.toString(arr));
	}
}