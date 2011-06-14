import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;
public class ShowAllBooks {
    public void ShowAll()
    {
        String output="";
        try
        {
        FileReader f=new FileReader("/home/xyf/Desktop/src/BookCatalogue.vim");
        BufferedReader input = new BufferedReader (f);
        StringBuffer buffer = new StringBuffer();
        int number=0;
        String text;
        while((text = input.readLine()) != null)
        {
              buffer.append(text +"\n");
              number++;
        }
        output = buffer.toString();
        System.out.println("The total number of books is:"+number);
       
        String message=String.format("%-15s%-15s%-15s","Name","author","press");
        System.out.println(message);
       
        System.out.println(output);
        input.close();
        f.close();
        }
        catch(IOException e)
        {
            e.printStackTrace();
        }
        System.out.print("b)Back OR e)Exit:");
        Scanner s=new Scanner(System.in);
        String which=s.next();
        if(which.equalsIgnoreCase("b"))
        {
            Select st=new Select();
            st.SelectService();
        }
        else
        {
            return;
        }
    }
}