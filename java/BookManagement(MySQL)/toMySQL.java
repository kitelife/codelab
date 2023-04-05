import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
public class toMySQL {
	public static Connection getConnection() throws SQLException, InstantiationException, IllegalAccessException, ClassNotFoundException {
		
			Class.forName("com.mysql.jdbc.Driver").newInstance();
			
			String url="jdbc:mysql://localhost/BookManagement?useUnicode=true&characterEncoding=utf-8";
			String username = "root";
			String password = "06122553";
		return DriverManager.getConnection(url, username, password);
	}
}