import java.util.Scanner;
public class Select {
    ReturnBook rb=new ReturnBook();
    InquireBook ib=new InquireBook();
    LendBook lb=new LendBook();
    ShowAllBooks sab=new ShowAllBooks();
    AddBook ab=new AddBook();
    ShowLentBooks slb=new ShowLentBooks();
    public void SelectService()
    {
        System.out.println("1.Show all the books\n2.Inquire book\n3.Lend book\n4.Return book\n5.Add book\n" +
        "6.Show lent books");
        System.out.print("Please select one from services listed above:");
        Scanner s=new Scanner(System.in);
        int selectNumber=s.nextInt();
       
        if(selectNumber==1)
        {
            sab.ShowAll();
        }
        else if(selectNumber==2)
        {
            ib.Inquire();
        }
        else if(selectNumber==3)
        {
            lb.Lend();
        }
        else if(selectNumber==4)
        {
            rb.returnBook();
        }
        else if(selectNumber==5)
        {
            ab.add();
        }
        else if(selectNumber==6)
        {
            slb.ShowLent();
        }
        else
        {
            System.out.println("Input error,Please select one from services listed below again.");
            Select ss=new Select();
            ss.SelectService();
        }
    }
}