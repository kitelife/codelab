import java.io.File;
import java.io.IOException;

public class CreateFileInNewDir {

    public static void main(String[] args){
        if(args.length > 0){
            File file = new File(args[0]);
            if(!file.getParentFile().exists()){
                file.getParentFile().mkdir();
            }
            else if(!file.exists()){
                try{
                    file.createNewFile();
                }catch(IOException e){
                    e.printStackTrace();
                }
            }
        }
    }
}