<%@ page language="java" contentType="text/html; charset=GBK" pageEncoding="GBK"%>
<%@ taglib prefix="s" uri="/struts-tags" %>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    
    <title>Login Page</title>
  </head>
  
  <body>
    <s:form action="login">
    	<s:textfield name="username" />
    	<s:textfield name="password" />
    	<s:submit />
    </s:form>
  </body>
</html>
