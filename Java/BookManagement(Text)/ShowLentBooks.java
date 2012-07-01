import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;
public class ShowLentBooks {
    public void ShowLent()
    {
        String output="";
        try
        {
            File fs=new File("LentBookCatalogue.vim");
            if(!fs.exists())
            {
                System.out.println("The file is not exist");
            }
            else
            {
            FileReader f=new FileReader(fs);
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
        System.out.println("The number of Lent books is:"+number);
       
        String message=String.format("%-10s%-10s%-20s%-15s%-20s", "Name","Author","Press","Who","Time");
        System.out.println(message);
       
        System.out.println(output);
        input.close();
        f.close();
            }
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
