import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;
public class ShowLentBooks {
	public void ShowLent() throws SQLException, InstantiationException,
			IllegalAccessException, ClassNotFoundException {
		Connection conn = toMySQL.getConnection();
		String s1 = "*********************************************************************************************";
		String s2 = "---------------------------------------------------------------------------------------------";
		try {
			Statement stat = conn.createStatement();
			ResultSet result = stat.executeQuery("SELECT * FROM lentbooks");
			
			System.out.println(s1);
			System.out.printf("%-38s%-25s%-30s", " Name","Who","Time");
			System.out.println("\n"+s1);
			
			if (!result.isBeforeFirst())
				System.out.println("No book has been lent!");
			else {	
				while (result.next()) {
					String s21=result.getString(1),s22=result.getString(2),s23=result.getString(3);
					System.out.printf("%-30s%-25s%-30s"," "+s21,s22,s23);
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
		System.out.print("b)Back OR e)Exit:");
		Scanner ss = new Scanner(System.in);
		String which = ss.next();
		if (which.equalsIgnoreCase("b")) {
			Select st = new Select();
			st.SelectService();
		} else {
			return;
		}
	}
}