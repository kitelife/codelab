package demo;

import com.opensymphony.xwork2.Action;

public class LoginAction implements Action{

	private String username;
	private String password;
	
	private String tip;

	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public String getTip() {
		return tip;
	}

	public void setTip(String tip) {
		this.tip = tip;
	}
	
	public String execute() throws Exception{
		if(getUsername().equalsIgnoreCase("user")){
			throw new MyException("自定义异常");
		}
		if(getUsername().equalsIgnoreCase("sql")){
			throw new java.sql.SQLException("用户名不能为SQL");
		}
		if(getUsername().equals("crazyit.org") && getPassword().equals("leegang")){
			setTip("哈哈，服务器提示!");
			return SUCCESS;
		}else{
			return ERROR;
		}
	}
}
