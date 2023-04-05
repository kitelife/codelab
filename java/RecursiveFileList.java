import java.io.File;

public class RecursiveFileList {

    public static void main(String[] args) {
        if(args.length > 0){
            File file = new File(args[0]);
            fileList(file);
        }
    }

    static void fileList(File file){
        if(file.isDirectory()) {
            File lists[] = file.listFiles();
            if(lists != null){
                for(File f : lists){
                    fileList(f);
                }
            }
        }
        System.out.println(file);
    }
}