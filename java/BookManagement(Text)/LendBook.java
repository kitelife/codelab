import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Date;
import java.util.Scanner;
public class LendBook {
    Scanner s=new Scanner(System.in);
    public void Lend()
    {
        try {
            System.out.print("Please input name of the book you will lend:");
            String name = s.nextLine();
           
            System.out.print("Please input who:");
            String who=s.nextLine();
           
            FileReader f = new FileReader("BookCatalogue.vim");
            FileWriter fw=new FileWriter("LentBookCatalogue.vim",true);
           
            BufferedReader input = new BufferedReader(f);
            BufferedWriter bw=new BufferedWriter(fw);
           
            String text;
            while (((text = input.readLine()) != null)) {
                if(text.contains(name))
                {
                    String message=String.format("%-45s%-15s%-20s",text,who,new Date());
                    bw.write(message);
                }
            }
            bw.newLine();
           
            bw.flush();
            bw.close();
            fw.close();
            input.close();
            f.close();
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
        System.out.print("a)Again OR b)Back OR e)Exit:");
        String which=s.nextLine();
        if(which.equalsIgnoreCase("a"))
        {
            LendBook lb=new LendBook();
            lb.Lend();
        }
        else if(which.equalsIgnoreCase("b"))
        {
            Select ss=new Select();
            ss.SelectService();
        }
    }
}
