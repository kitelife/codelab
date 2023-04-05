import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;
public class InquireBook {
    Scanner s = new Scanner(System.in);
    public void Inquire() {
        try {
            System.out.print("Input the book's name:");
            String name = s.nextLine();
           
            FileReader f = new FileReader("BookCatalogue.vim");
            BufferedReader input = new BufferedReader(f);
            String text;
            while (((text = input.readLine()) != null)) {
                if(text.contains(name))
                 System.out.println(text);
            }
            input.close();
            f.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.print("a)Again OR b)Back OR e)Exit:");
        String which=s.next();
        if(which.equalsIgnoreCase("a"))
        {
            InquireBook ib=new InquireBook();
            ib.Inquire();
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
