import java.util.Date;
import java.util.Scanner;
 
public class Welcome {
    /**
     * @param args
     * @throws IOException 
     */
    public static void main(String[] args){
        // TODO Auto-generated method stub
 
        System.out.println("Welcome to visit software of book management!\n");
        System.out.println("Now is "+new Date()+"\n");
        Select s=new Select();
        s.SelectService();
    }
}