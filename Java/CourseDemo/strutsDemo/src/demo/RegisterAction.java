package demo;

import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

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
		try {
			//Session sess = HibernateUtil.currentSession();
			Configuration conf = new Configuration().configure();
			SessionFactory sf = conf.buildSessionFactory();
			Session sess = sf.openSession();
			Transaction tx = sess.beginTransaction();
			User user = (User) sess.get(User.class, username);

			if (user != null) {
				return INPUT;
			} else {
				user = new User();
				user.setUsername(username);
				user.setPassword(password);
				user.setEmail(email);
				sess.save(user);
				tx.commit();
				return SUCCESS;
				// return LOGIN;
			}
		} catch (HibernateException e) {
			throw e;
		} finally {
			HibernateUtil.closeSession();
		}
	}
}
