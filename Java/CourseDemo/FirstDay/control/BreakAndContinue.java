package control;

public class BreakAndContinue {
	static int[] range(int num){
		int[] rangeArray = new int[20];
		for(int index = 0; index < 20; index++)
			rangeArray[index] = index;
		return rangeArray;
		
	}
	public static void main(String[] args) {
		for(int index = 0; index < 20; index++) {
			if(index == 15) break; // 退出循环
			if(index % 2 != 0 ) continue; // 如果index不被2整除，则跳过本次循环接下来的语句，直接进行下一次循环
			System.out.println(index + " ");
		}
		System.out.println();
		// 使用foreach
		for(int index : range(20)){
			if(index == 15) break; // 退出循环
			if(index % 2 != 0 ) continue; // 如果index不被2整除，则跳过本次循环接下来的语句，直接进行下一次循环
			System.out.println(index + " ");
		}
		// 貌似无限循环
		int index = 0;
		while(true){
			index++;
			int j = index * 42;
			if(j == 4242) break;
			if(index % 10 != 0) continue;
			System.out.println(index + " ");
		}
	}
}
