package control;

import java.util.*;

public class ForEachInt {

	/**
	 * @param args
	 */
	public static void main(String[] args) {

		// 关键字new
		Random rand = new Random(3);
		int intArray[] = new int[10];
		for(int index = 0; index < 10; index++)
			intArray[index] = rand.nextInt(100);
		int inA[] = {30,63,48,84,70,25,5,18,19,93};
		//System.out.println(intArray.toString());
		for(int num : intArray)
			System.out.println(num);

		for(int num : inA)
			System.out.print(num + " ");
		System.out.println();
	}
}