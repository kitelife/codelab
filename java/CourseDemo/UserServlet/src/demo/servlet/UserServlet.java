package demo.servlet;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

public class UserServlet extends HttpServlet{

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String method = (String)request.getParameter("method");
		if(method==null){
			PrintWriter out = response.getWriter();
			out.println("invalid request!");
		}else if(method.equals("login")){
			Login(request, response);
		}else if(method.equals("logout")){
			Logout(request, response);
		}else if(method.equals("register")){
			Register(request, response);
		}
	}
	
	protected void Login(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException{
		String username = request.getParameter("username");
		String password = request.getParameter("password");
		
		if(username == null || password == null){
			response.sendRedirect("login.jsp");
			return;
		}
		
		UserBean userBean = new UserBean();
		boolean isValid = userBean.valid(username, password);
		if(isValid){
			HttpSession session = request.getSession();
			session.setAttribute("username", username);
			response.sendRedirect("welcome.jsp");
			return;
		}else{
			response.sendRedirect("login.jsp");
			return;
		}
	}
	protected void Logout(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException{
		HttpSession session = request.getSession();
		session.removeAttribute("username");
		response.sendRedirect("login.jsp");
	}
	
	protected void Register(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException{
	
		String username = request.getParameter("username");
		String password1 = request.getParameter("password1");
		String password2 = request.getParameter("password2");
		String email = request.getParameter("email");
		
		if(username == null || password1 == null || password2 == null || !password1.equals(password2)){
			response.sendRedirect("register.jsp");
			return;
		}
		
		UserBean userBean = new UserBean();
		boolean isExist = userBean.isExist(username);
		if(!isExist){
			userBean.add(username, password1, email);
			response.sendRedirect("login.jsp");
			return;
		}else{
			response.sendRedirect("register.jsp");
			return;
		}
	}
}
