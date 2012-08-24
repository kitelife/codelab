<%@ page import="java.sql.Connection" %>
<%@ page import="java.sql.DriverManager" %>
<%@ page import="java.sql.Statement" %>
<%@ page import="java.sql.ResultSet" %>
<%@ page import="java.sql.ResultSetMetaData" %>

<%
String drv = "org.gjt.mm.mysql.Driver";
String url = "jdbc:mysql://localhost:3306/sample";
String usr = "root";
String pwd = "xiayf";
%>