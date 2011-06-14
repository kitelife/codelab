import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;
public class ReturnBook {
	Scanner s = new Scanner(System.in);
	public void returnbook() throws SQLException, InstantiationException, IllegalAccessException, ClassNotFoundException
	{
		System.out.print("Please input the book's name:");
		String name=s.nextLine();
		
		Connection conn=toMySQL.getConnection();
		try
		{
			Statement stat=conn.createStatement();
			stat.executeUpdate("DELETE FROM lentbooks WHERE bookname="+"'"+name+"'");
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}
		finally
		{
			conn.close();
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