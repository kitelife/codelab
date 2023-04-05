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
			<form name="form1" action="UserServlet.do?method=logout" method="post">
				<table width="200" border="1">
					<tr>
						<td colspan="2">Login Success</td>
					</tr>
					<tr>
						<td>Welcome</td>
						<td><%=(String)session.getAttribute("username") %></td>
					</tr>
					<tr>
						<td colspan="2">
							<input type="submit" name="submit" value="Logout" />
						</td>
					</tr>
				</table>
			</form>
		</td>
	</tr>
</table>