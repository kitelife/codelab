import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;
public class ReturnBook {
    Scanner s = new Scanner(System.in);
    public void returnBook()
    {
        System.out.print("Please input the book's name:");
        String name=s.nextLine();
        try
        {
            FileReader f=new FileReader("LentBookCatalogue.vim");
            BufferedReader reader=new BufferedReader(f);
           
            StringBuffer buffer = new StringBuffer();
            String text;
           
            while((text = reader.readLine()) != null)
            {
                //System.out.println(text);
                if(text.contains(name))
                {
                    text="";
                    buffer.append(text);
                }
                else
                {
                    buffer.append(text +"\n");
                }
            }
            String output;
            output=buffer.toString();
            //System.out.println(output);
           
            FileWriter fw=new FileWriter("LentBookCatalogue.vim");
            BufferedWriter writer=new BufferedWriter(fw);
            writer.write(output);
         
            reader.close();
            f.close();
            writer.flush();
            writer.close();
            fw.close();
        }
        catch(IOException e)
        {
            e.printStackTrace();
        }
        System.out.print("a)Again OR b)Back OR e)Exit:");
        String which=s.next();
        if(which.equalsIgnoreCase("a"))
        {
            ReturnBook rb=new ReturnBook();
            rb.returnBook();
        }
        else if(which.equalsIgnoreCase("b"))
        {
            Select s=new Select();
            s.SelectService();
        }
        else
        {
            return ;
        }
    }
}
