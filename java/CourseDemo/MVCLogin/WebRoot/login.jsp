
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
	<title>Login Page</title>
  </head>
  
  <body>
  	<span style="color:red; font-weight:bold">
  		<%
  			if(request.getAttribute("err") != null){
  				out.println(request.getAttribute("err") + "<br />");
  			}
  		%>
  	</span>
  	<form id="login" method="post" action="login">
  		用户名: <input type="text" name="username" /><br />
  		密&nbsp;&nbsp;码: <input type="password" name="pass" /><br />
  		<input type="submit" value="登录" /><br />
  	</form>
  </body>
</html>
