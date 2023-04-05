package ObjectOriented;

class SupClass{
	public void someFunction(){
	}
}

class subClass1 extends SupClass {
	public void someFunction(){
		System.out.println("This object's class is subClass1");
	}
}

class subClass2 extends SupClass {
	public void someFunction() {
		System.out.println("This object's class is subClass2");
	}
}

class TestClass {
	static void testFunction(SupClass sc){
		sc.someFunction();
	}
}

public class DuoTai {
	public static void main(String[] args) {
		SupClass sc1 = new subClass1();
		SupClass sc2 = new subClass2();
		TestClass.testFunction(sc1);
		TestClass.testFunction(sc2);
	}
}
