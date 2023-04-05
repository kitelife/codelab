import java.io.File;

public class IsFile {

    public static void main(String[] args){

        //System.out.println(args[0]);
        for(String s : args){
            System.out.println(s);
        }

        File f1 = new File(args[0]);
        File f2 = new File(args[1]);
        System.out.println(f1.isFile());
        System.out.println(f2.isDirectory());
        System.out.println(f2.isFile());
    }
}