package control;

public class ReturnSample {
    public static int getValue(){
        return 42;
    }

    public static void main(String[] args){
        int fromGetValue = getValue();
        System.out.println(fromGetValue);
    }
}