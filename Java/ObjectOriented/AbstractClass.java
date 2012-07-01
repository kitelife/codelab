package ObjectOriented;

abstract class BaseClass {
	abstract void functionOne();
	abstract void functionTwo();
	void functionThree(){
		System.out.println("BaseClass functionThree");
	};
}

class SubClass extends BaseClass{
	void functionOne() {
		System.out.println("functionOne");
	}
	
	void functionTwo() {
		System.out.println("functionTwo");
	}
	/*
    void functionThree(){
    	System.out.println("SubClass functionThree");
    }
    */
}

public class AbstractClass {
	public static void main(String[] args){
		SubClass sc = new SubClass();
		sc.functionOne();
		sc.functionTwo();
		sc.functionThree();
	}
}
