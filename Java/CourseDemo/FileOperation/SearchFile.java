import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

public class SearchFile {

    static ArrayList<String> arrayList;

    public static void main(String[] args){

        arrayList = new ArrayList<String>();

        if(args.length > 1){
            File file = new File(args[0]);
            fileList(file);
            int matchCount = 0;
            for(String s : arrayList){
                String[] pathParts = s.split(File.separator);
                if(pathParts[pathParts.length - 1].contains(args[1])){
                    matchCount++;
                    System.out.println(s);
                }
            }
            System.out.println("找到匹配的文件数量：" + matchCount);
        }else{
            System.out.println("Usage: java SearchFile pathname filename");
        }
    }

    static void fileList(File file){
        if(file.isDirectory()){
            File[] files = file.listFiles();
            for(File f : files){
                fileList(f);
                try {
                    arrayList.add(f.getCanonicalPath());
                } catch (IOException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }
            }
        }
        //System.out.println(file);
    }
}