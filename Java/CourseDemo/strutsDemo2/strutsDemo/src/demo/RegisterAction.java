package demo;

import java.sql.ResultSet;

import com.opensymphony.xwork2.ActionSupport;

public class RegisterAction extends ActionSupport {

	private String username;
	private String password;
	private String passwordEnsure;
	private String email;

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

	public String getPasswordEnsure() {
		return passwordEnsure;
	}

	public void setPasswordEnsure(String passwordEnsure) {
		this.passwordEnsure = passwordEnsure;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String execute() throws Exception {
		String username = getUsername();
		String password = getPassword();
		String passwordEnsure = getPasswordEnsure();
		String email = getEmail();
		if (username == null || password == null || passwordEnsure == null
				|| email == null || !password.equals(passwordEnsure)) {
			return INPUT;
		}
		DbDao dd = new DbDao("com.mysql.jdbc.Driver",
				"jdbc:mysql://localhost:3306/demo", "root", "xiayf");
		ResultSet rs = dd.query("select * from user where username = ?",
				username);
		if (rs.next()) {
			return INPUT;
		} else {
			dd.insert(
					"insert into user(username, password, email)values(?,?,?)",
					username, password, email);
			return SUCCESS;
			//return LOGIN;
		}
	}
}
