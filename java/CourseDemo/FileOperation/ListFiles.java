import java.io.File;

public class ListFiles {

    public static void main(String[] args){
        File file = new File(args[0]);
        File path[] = file.listFiles();
        for(File f : path){
            System.out.println(f.getPath());
        }
    }
}