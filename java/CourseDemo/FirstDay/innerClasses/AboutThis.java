package innerClasses;

public class AboutThis {
	void someFunction(){
		System.out.println("aboutThis.someFunction()");
	}
	public class Inner {
		public AboutThis outer(){
			return AboutThis.this;
		}
	}
	public Inner getInner(){
		return new Inner();
	}
	public static void main(String[] args){
		AboutThis at = new AboutThis();
		AboutThis.Inner ati = at.getInner();
		ati.outer().someFunction();
	}
}
