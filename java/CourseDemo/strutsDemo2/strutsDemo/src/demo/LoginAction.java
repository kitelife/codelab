package demo;
import java.sql.ResultSet;

import com.opensymphony.xwork2.ActionContext;
import com.opensymphony.xwork2.ActionSupport;


public class LoginAction extends ActionSupport{

	/**
	 * 
	 */
	private String username;
	private String password;
	private String tip;
	
	public String getUsername(){
		return username;
	}
	
	public void setUsername(String username){
		this.username = username;
	}
	
	public String getPassword(){
		return password;
	}
	
	public void setPassword(String password){
		this.password = password;
	}
	public String getTip() {
		return tip;
	}

	public void setTip(String tip) {
		this.tip = tip;
	}

	// ���崦���û������execute����
	@Override
	public String execute() throws Exception{
		String username = getUsername();
		String password = getPassword();
		DbDao dd = new DbDao("com.mysql.jdbc.Driver",
				"jdbc:mysql://localhost:3306/demo", "root", "xiayf");
		ResultSet rs = dd.query(
				"select password from user where username = ?", username);
		if(rs.next()){
			if(rs.getString("password").equals(password)){
				ActionContext.getContext().getSession().put("user", getUsername());
				setTip("�ɹ���¼");
				return SUCCESS;
			}
			else{
				setTip("���벻��ȷ");
				return INPUT;
			}
		}else{
			setTip("�����ڴ��û�");
			return INPUT;
		}
	}
}
