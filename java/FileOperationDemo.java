import java.io.File;
import java.io.IOException;

public class FileOperationDemo {

    public static void main(String[] args) {
        System.out.println(File.separator);
        File file = new File("demo.txt");
        if(file.exists()) {
            file.delete();
        } else {
            try{
                file.createNewFile();
            } catch(IOException e){
                e.printStackTrace();
            }
        }
    }
}