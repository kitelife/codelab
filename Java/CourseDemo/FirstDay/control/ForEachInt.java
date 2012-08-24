package control;

import java.util.*;

public class ForEachInt {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		
		// 关键字new
		Random rand = new Random(42);
		int intArray[] = new int[10];
		for(int index = 0; index < 10; index++)
			intArray[index] = rand.nextInt(100);
		for(int num : intArray)
			System.out.println(num);
	}

}
