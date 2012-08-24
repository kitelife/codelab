package demo.servlet;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class DBAccess {
	private String drv = "org.gjt.mm.mysql.Driver";
	private String url = "jdbc:mysql://localhost:3306/demo";
	private String usr = "root";
	private String passwd = "xiayf";
	private Connection conn = null;
	private Statement stm = null;
	private ResultSet rs = null;
	
	public Connection getConn() {
		return conn;
	}
	public void setConn(Connection conn) {
		this.conn = conn;
	}
	public Statement getStm() {
		return stm;
	}
	public void setStm(Statement stm) {
		this.stm = stm;
	}
	public ResultSet getRs() {
		return rs;
	}
	public void setRs(ResultSet rs) {
		this.rs = rs;
	}
	public String getDrv() {
		return drv;
	}
	public void setDrv(String drv) {
		this.drv = drv;
	}
	public String getUrl() {
		return url;
	}
	public void setUrl(String url) {
		this.url = url;
	}
	public String getUsr() {
		return usr;
	}
	public void setUsr(String usr) {
		this.usr = usr;
	}
	public String getPasswd() {
		return passwd;
	}
	public void setPasswd(String passwd) {
		this.passwd = passwd;
	}
	
	public boolean createConn(){
		boolean b = false;
		try{
			Class.forName(drv).newInstance();
			conn = DriverManager.getConnection(url, usr, passwd);
			b = true;
		}catch(Exception e){
			e.printStackTrace();
		}
		return b;
	}
	
	public boolean update(String sql){
		boolean b = false;
		try{
			stm = conn.createStatement();
			stm.execute(sql);
			b = true;
		}catch(Exception e){
			e.printStackTrace();
		}
		return b;
	}
	
	public void query(String sql){
		try{
			stm = conn.createStatement();
			rs = stm.executeQuery(sql);
		}catch(Exception e){
			e.printStackTrace();
		}
	}
	
	public boolean next(){
		boolean b = false;
		try{
			if(rs.next()){
				b = true;
			}
		}catch(Exception e){
			
			e.printStackTrace();
		}
		return b;
	}
	public String getValue(String field){
		String value = null;
		try{
			if(rs!=null)
				value = rs.getString(field);
		}catch(Exception e){
			e.printStackTrace();
		}
		return value;
	}
	public void closeRs(){
		try{
			if(rs != null)
				rs.close();
		}catch(Exception e){
			e.printStackTrace();
		}
	}
	
	public void closeStm(){
		try{
			if(stm != null)
				stm.close();
		}catch(Exception e){
			e.printStackTrace();
		}
	}
	
	public void closeConn(){
		try{
			if(conn != null)
				conn.close();
		}catch(Exception e){
			e.printStackTrace();
		}
	}
}
