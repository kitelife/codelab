<form name="form1" action="register_action.jsp" method="post">
	<table width="200" border="1">
		<tr>
			<td colspan="2">注册窗口</td>
		</tr>
		<tr>
			<td>用户名</td>
			<td><input type="text" name="username" size="10" /></td>
		</tr>
		<tr>
			<td>密码</td>
			<td><input type="password" name="password1" size="10" /></td> 
		</tr>
		<tr>
			<td>确认密码</td>
			<td><input type="password" name="password2" size="10" /></td>
		</tr>
		<tr>
			<td>Email</td>
			<td><input type="text" name="email" size="10" /></td>
		</tr>
		<tr>
			<td colspan="2">
				<input type="submit" name="submit" value="注册" />
				<a href="login.jsp">登录</a>
			</td>
		</tr>
	</table>
</form>