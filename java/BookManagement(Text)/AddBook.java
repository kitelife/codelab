import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;

public class AddBook {
    Scanner s=new Scanner(System.in);
    public void add()
    {
        System.out.print("Please input the book's name:");
        String name=s.next();
        System.out.print("Please input the author:");
        String author=s.next();
        System.out.print("Please input the press:");
        String press=s.next();
        try
        {
            FileWriter fw=new FileWriter("BookCatalogue.vim",true);
            BufferedWriter bw=new BufferedWriter(fw);
            String message=String.format("%-15s%-15s%-15s",name,author,press);
            bw.write(message);
            bw.newLine();
           
            bw.flush();
            bw.close();
            fw.close();
        }
        catch(IOException e)
        {
            e.printStackTrace();
        }
        System.out.print("a).Again OR b)Back OR e)Exit:");
        String which=s.next();
        if(which.equalsIgnoreCase("a"))
        {
            AddBook ab=new AddBook();
            ab.add();
        }
        else if(which.equalsIgnoreCase("b"))
        {
            Select st=new Select();
            st.SelectService();
        }
        else
        {
            return ;
        }
    }
}
