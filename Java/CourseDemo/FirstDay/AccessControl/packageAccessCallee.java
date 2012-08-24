package AccessControl;

class Callee {
	void printSomeMessage(String msg){
		System.out.println(msg);
	}
}
public class packageAccessCallee {

	public static void main(String[] args){
		Callee ce = new Callee();
		ce.printSomeMessage("Hello, packageAccessControl");
	}
}
