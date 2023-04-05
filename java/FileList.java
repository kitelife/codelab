import java.io.File;
public class FileList {

    public static void main(String[] args){
        File file = new File(args[0]);
        String path[] = file.list();
        for(String p : path)
            System.out.println(p);
    }
}