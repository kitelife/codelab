import java.sql.SQLException;
import java.util.Date;
public class Welcome {
	/**
	 * @param args
	 * @throws SQLException 
	 * @throws ClassNotFoundException 
	 * @throws IllegalAccessException 
	 * @throws InstantiationException 
	 */
	public static void main(String[] args) throws SQLException, InstantiationException, IllegalAccessException, ClassNotFoundException {
		// TODO Auto-generated method stub
		System.out.println("Welcome to visit software of book management!\n");
		System.out.println("Now is "+new Date()+"\n");
		Select s=new Select();
	    s.SelectService();
	} 
}