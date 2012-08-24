<table width="100%">
	<tr>
		<td>
			<img src="images/logo4.png" />
		</td>
		<td>
			<img src="images/logo2.png" />
		</td>
	</tr>
	<tr>
		<td colspan="2">
			<hr>
		</td>
	</tr>
	<tr>
		<td>
			<table>
				<tr>
					<td><a href="welcome.jsp">Main</a></td>
				</tr>
				<tr>
					<td><a href="menu1.jsp">Menu1</a></td>
				</tr>
			</table>
		</td>
		<td>
			<form name="form1" action="logout.jsp" method="post">
				<table width="200" border="1">
					<tr>
						<td colspan="2">登录成功</td>
					</tr>
					<tr>
						<td>欢迎您，</td>
						<td><%=(String)session.getAttribute("username") %></td>
					</tr>
					<tr>
						<td colspan="2">
							<input type="submit" name="submit" value="退出" />
						</td>
					</tr>
				</table>
			</form>
		</td>
	</tr>
</table>