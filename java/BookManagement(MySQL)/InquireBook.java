import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;
public class InquireBook {
	Scanner s = new Scanner(System.in);
	public void Inquire() throws SQLException, InstantiationException,
			IllegalAccessException, ClassNotFoundException {
		Connection conn = toMySQL.getConnection();
		
		String s1="************************************************************************";
		String s2="------------------------------------------------------------------------";
		
		try {
			System.out.print("Input the book's name:");
			String name = s.nextLine();
			Statement stat = conn.createStatement();
			ResultSet result = stat
					.executeQuery("SELECT * FROM allbooks WHERE bookname LIKE '%"
							+name + "%'");
			
			System.out.println(s1);
			System.out.printf("%-35s%-25s%-30s"," Name","Author","Press");
			System.out.println();
			System.out.println(s1);
			
			if (!result.isBeforeFirst())
				System.out.println("There is no book you want.");
			else {
				while (result.next()) {
					
					System.out.printf("%-30s%-25s%-30s", " "+result.getString(1),result.getString(2),result.getString(3));
					System.out.println();
				}
				System.out.println(s2);
			}
			result.close();
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			conn.close();
		}
		System.out.print("a)Again OR b)Back OR e)Exit:");
		String which = s.next();
		if (which.equalsIgnoreCase("a")) {
			InquireBook ib = new InquireBook();
			ib.Inquire();
		} else if (which.equalsIgnoreCase("b")) {
			Select s = new Select();
			s.SelectService();
		} else {
			return;
		}
	}
}