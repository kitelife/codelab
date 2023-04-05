package exceptions;
// Creating your own exceptions

class SimpleException extends Exception {}

public class InheritingException {
    public void f() throws SimpleException {
        System.out.println("Throw SimpleException from f()");
        throw new SimpleException();
    }

    public static void main(String[] args) {
        InheritingException sed = new InheritingException();
        try {
			sed.f();
		} catch (SimpleException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
        System.out.println("这句代码还执行么？");
    }
}