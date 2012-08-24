<%@ include file="inc.jsp" %>
<%
// 取得参数
String username = request.getParameter("username");
String password = request.getParameter("password");

// 检查是否为空
if(username == null || password == null){
	response.sendRedirect("login.jsp");
}

// 验证登录
boolean isValid = false;

String sql = "select * from user where name='" + username + "' and passwd = '" + password +"'";
try{
	Class.forName(drv).newInstance();
	Connection conn = DriverManager.getConnection(url, usr, pwd);
	Statement stm = conn.createStatement();
	ResultSet rs = stm.executeQuery(sql);
	if(rs.next())
		isValid = true;
	rs.close();
	stm.close();
	conn.close();
}catch(Exception e){
	e.printStackTrace();
	out.print(e);
}finally{
}

if(isValid){
	session.setAttribute("username", username);
	response.sendRedirect("welcome.jsp");
}else{
	response.sendRedirect("login.jsp");
}
%>