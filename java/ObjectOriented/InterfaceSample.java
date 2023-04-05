package ObjectOriented;

interface Interface1 {
	void function1One();
	void function1Two(String msg);
	void function1Three(String msg, int num);
}

interface Interface2 {
	void function2One(int num1, int num2);
}

class SomeClass implements Interface1, Interface2 {
	
	public void function1One(){
		System.out.println("This is in function1One");
	}
	
	public void function1Two(String msg){
		System.out.println(msg);
	}
	
	public void function2One(int num1, int num2){
		System.out.println(num1 + " + " + num2 + " = " + new Integer(num1+num2)); // 为什么需要new Integer()?
	}
	
	public void function1Three(String msg, int num2){
		System.out.println("msg: "+ msg + "; num2: "+ num2);
	}
}
public class InterfaceSample {

	public static void main(String[] args) {
		SomeClass sc = new SomeClass();
		sc.function1One();
		sc.function1Three("Hello sc", 100);
		sc.function1Two("Hello, World! I love you!");
		sc.function2One(177, 42);
	}
}
