<%--
��վ: <a href="http://www.crazyit.org">���Java����</a>
author  yeeku.H.lee kongyeeku@163.com
version  1.0
Copyright (C), 2001-2012, yeeku.H.Lee
This program is protected by copyright laws.
Program Name:
Date: 
--%>

<%@ page contentType="text/html; charset=GBK" language="java" errorPage="" %>
<%@taglib prefix="s" uri="/struts-tags"%>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<title>�û�ע��</title>
</head>
<body>
<h3>�û�ע��</h3>
<s:form action="registPro">
	<s:textfield name="person.name" label="�û���"/>
	<s:textfield name="person.age" label="����"/>
	<tr>
		<td colspan="2">
		<s:submit value="ע��" theme="simple"/>
		<s:reset value="����" theme="simple"/></td>
	</tr>
</s:form>
</body>
</html>
