<?php
require_once('config.php');
require_once('view_functions.php');
require_once('auth_functions.php');
session_start();

@$UserName=$_POST['UserName'];
@$Password=$_POST['Password'];

$UserName=trim($UserName);
$Password=trim($Password);
if(!get_magic_quotes_gpc())
{
	$UserName=addslashes($UserName);
	$Password=addslashes($Password);
}
if($UserName && $Password)
{
	try{
		login($UserName, $Password);
		$_SESSION['valid_user']=$UserName;
	}
	catch(Exception $e)
	{
		do_html_header($title);
		echo 'You could not log in, 
			and you must log in to view this page!';
		do_html_footer();
		exit;
	}
}
if(isset($_SESSION['valid_user']))
{
	do_html_header($title);
	display_console_form();
	echo '<br /><br /><center><div font="5">';
	echo '<a href="main.php">main</a>&nbsp&nbsp';
	echo '<a href="logout.php">Logout</a>';
	echo '</div></center>';
	do_html_footer();
}
else
{
	do_html_header($title);
	echo 'you have no permission!<br /><br />';
	echo '<a href="main.php">main</a>&nbsp&nbsp';
	echo '<a href="login.php">Login</a>';
	do_html_footer();
}
?>
