<%@ page language="java" contentType="text/html; charset=GBK" pageEncoding="GBK"%>
<%@ taglib prefix="s" uri="/struts-tags" %>
<html>
<head>
<title><s:text name="registerPage" /></title>
</head>
<body>
<s:form action="register">
	<s:textfield name="username" key="user" />
	<s:textfield name="password" key="pass" />
	<s:textfield name="passwordEnsure" key="passensure" />
	<s:textfield name="email" key="email" />
	<s:submit key="register" />
</s:form>
</body>
</html> 