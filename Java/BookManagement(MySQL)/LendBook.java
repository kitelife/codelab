import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Date;
import java.util.Scanner;
public class LendBook {
	Scanner s=new Scanner(System.in);
	public void Lend() throws SQLException, InstantiationException, IllegalAccessException, ClassNotFoundException
	{
		Connection conn = toMySQL.getConnection();
		try {
			System.out.print("Please input name of the book you will lend:");
			String name = s.nextLine();
			
			System.out.print("Please input who:");
			String who=s.nextLine();
			
			Statement stat = conn.createStatement();
			stat.executeUpdate("INSERT INTO lentbooks VALUES(" + "'"+name+"','" +who+"','"+ new Date()+"'"+ ")");
		} 
		catch (Exception e)
		{
			e.printStackTrace();
		}
		finally
		{
			conn.close();
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