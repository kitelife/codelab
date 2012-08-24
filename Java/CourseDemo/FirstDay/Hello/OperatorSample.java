public class OperatorSample {

    static void print(Object ob){
        System.out.println(ob);
    }

    public static void main(String[] args){
        print("Hello, World");
        int a = 42;
        print("原来的a=" + a);
        int b = 4242;
        a = a + b;
        // a += b;
        print("a加上b然后赋值给a之后, a= " + a);
        a++;
        print("a自增之后的值为：" + a);
        int c = a++;
        print("先把a赋值给c，然后自增，c = " + c);
        a--;
        c = ++a;
        print("a先自增，然后赋值给c, c = " + c);
        /*
        int unInit;
        print("unInit = " + unInit);
        */
        /*
        if(a > b)
            print("a大于b");
        else if(a < b)
            print("a小于b");
        else
            print("a等于b");
        */
        String someValue = a > b ? "a大于b" : "a小于等于b";
        print(someValue);
        print(a > b);
    }
}