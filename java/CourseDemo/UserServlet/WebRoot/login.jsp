<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <title>My JSP 'login.jsp' starting page</title>
    
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    
	<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
	<meta http-equiv="description" content="This is my page">
	<!--
	<link rel="stylesheet" type="text/css" href="styles.css">
	-->

  </head>
  
  <body>
    <form name="form1" action="UserServlet.do?method=login" method="post">
    	<table width="200" border="1">
    		<tr>
    			<td colspan="2">Login Window</td>
    		</tr>
    		<tr>
    			<td>User Name</td>
    			<td><input type="text" name="username" size="10" /></td>
    		</tr>
    		<tr>
    			<td>Your Password</td>
    			<td><input type="password" name="password" size="10" /></td>
    		</tr>
    		<tr>
    			<td colspan="2">
    				<input type="submit" name="submit" value="Login" />
    				<a href="register.jsp">Register New</a>
    			</td>
    		</tr>
    	</table>
    </form>
  </body>
</html>
