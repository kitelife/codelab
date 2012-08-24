package AccessControl;

public class packageAccessCaller {
	public static void main(String[] args){
		Callee ce = new Callee();
		ce.printSomeMessage("This is in class packageAccessCaller");
	}
}
