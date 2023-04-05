<form name="form1" action="UserServlet.do?method=register" method="post">
	<table width="200" border="1">
		<tr>
			<td colspan="2">Register Window</td>
		</tr>
		<tr>
			<td>User Name</td>
			<td><input type="text" name="username" size="10" /></td>
		</tr>
		<tr>
			<td>Password</td>
			<td><input type="password" name="password1" size="10" /></td> 
		</tr>
		<tr>
			<td>Re-Password</td>
			<td><input type="password" name="password2" size="10" /></td>
		</tr>
		<tr>
			<td>Email</td>
			<td><input type="text" name="email" size="10" /></td>
		</tr>
		<tr>
			<td colspan="2">
				<input type="submit" name="submit" value="Login" />
				<a href="login.jsp">Back</a>
			</td>
		</tr>
	</table>
</form>