package demo;

import java.sql.ResultSet;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
//import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

//@WebServlet(name = "login", urlPatterns = { "/login" })
public class LoginServlet extends HttpServlet {

	public void service(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, java.io.IOException {
		String errMsg = "";
		RequestDispatcher rd;
		String username = request.getParameter("username");
		String pass = request.getParameter("pass");
		try {

			DbDao dd = new DbDao("com.mysql.jdbc.Driver",
					"jdbc:mysql://localhost:3306/demo", "root", "xiayf");
			ResultSet rs = dd.query(
					"select pass from user_table where name = ?", username);
			if (rs.next()) {
				if (rs.getString("pass").equals(pass)) {
					HttpSession session = request.getSession(true);
					session.setAttribute("name", username);
					rd = request.getRequestDispatcher("/welcome.jsp");
					rd.forward(request, response);
				} else {
					errMsg += "您的用户名密码不符合，请重新输入";
				}
			} else {
				errMsg += "您的用户名不存在，请先注册";
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		if(errMsg != null && !errMsg.equals("")){
			rd = request.getRequestDispatcher("/login.jsp");
			request.setAttribute("err", errMsg);
			rd.forward(request, response);
		}
	}
}
