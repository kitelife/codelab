package innerClasses;
// Creating an inner class directly using the .new syntax

public class AboutNew {
	public class Inner {
		void printSomeValue(){
			System.out.println(42);
		}
	}
	public static void main(String[] args){
		AboutNew an = new AboutNew();
		//Inner ani = an.new Inner();
		AboutNew.Inner ani = an.new Inner();
		ani.printSomeValue();
	}
}
