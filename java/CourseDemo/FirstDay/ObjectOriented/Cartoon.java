package ObjectOriented;

class Art {
	// static方法就是没有this的方法，就是类方法。在static方法的内部不能调用非静态方法，反过来倒是可以的
	// 可以在没有创建任何对象的前提下，仅仅通过类本身来调用static方法。
	static String className;
    static void print(String msg) {
        System.out.println(msg);
    }

    Art() { print("Art constructor"); }
}

class Drawing extends Art {
    Drawing() { print("Drawing Constructor") ;}
}

public class Cartoon extends Drawing {
    public Cartoon() { print("Cartoon constructor"); }
    public static void main(String[] args) {
        Cartoon x = new Cartoon();
    }
}