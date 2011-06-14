import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;
public class AddBook {
	Scanner s = new Scanner(System.in);
	public void add() throws SQLException, InstantiationException, IllegalAccessException, ClassNotFoundException {
		System.out.print("Please input the book's name:");
		String name = s.nextLine();
		System.out.print("Please input the author:");
		String author = s.nextLine();
		System.out.print("Please input the press:");
		String press = s.nextLine();
		Connection conn = toMySQL.getConnection();
		try {
			Statement stat = conn.createStatement();
			stat.executeUpdate("INSERT INTO allbooks VALUES(" + "'"+name+"','" + 
					author+"','"+ press+"'"+ ")");
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			conn.close();
		}
		System.out.print("a).Again OR b)Back OR e)Exit:");
		String which = s.next();
		if (which.equalsIgnoreCase("a")) {
			AddBook ab = new AddBook();
			ab.add();
		} else if (which.equalsIgnoreCase("b")) {
			Select st = new Select();
			st.SelectService();
		} else {
			return;
		}
	}
}