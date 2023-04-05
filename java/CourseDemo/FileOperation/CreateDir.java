import java.io.File;

public class CreateDir {

    public static void main(String[] args) {

        if(args.length > 0){
            File file = new File(args[0]);
            file.mkdir();
        }else{
            System.out.println("You must input some directory name");
        }
    }
}