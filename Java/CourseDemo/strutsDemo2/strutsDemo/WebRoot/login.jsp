<%@ page language="java" contentType="text/html; charset=utf-8" pageEncoding="GBK"%>
<%@ taglib prefix="s" uri="/struts-tags" %>
<html>
<head>
<title><s:text name="loginPage" /></title>
</head>
<body>
<s:property value="tip"/>
<s:form action="login">
	<s:textfield name="username" key="user" />
	<s:textfield name="password" key="pass" />
	<s:submit key="login" />
</s:form>
</body>
</html> 