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
			throw new MyException("�Զ����쳣");
		}
		if(getUsername().equalsIgnoreCase("sql")){
			throw new java.sql.SQLException("�û�������ΪSQL");
		}
		if(getUsername().equals("crazyit.org") && getPassword().equals("leegang")){
			setTip("��������������ʾ!");
			return SUCCESS;
		}else{
			return ERROR;
		}
	}
}
