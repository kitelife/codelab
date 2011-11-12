<?php
require_once('config.php');
require_once('view_functions.php');
session_start();
$old_user = $_SESSION['valid_user'];
unset($_SESSION['valid_user']);
$result_dest = session_destroy();

do_html_header($title);
if(!empty($old_user))
{
	if($result_dest)
	{
		echo 'Logged out.<br /><br />';
		echo '<a href="main.php">main</a>&nbsp&nbsp';
		echo '<a href="login.php">Login</a>';

	}
}
do_html_footer();
?>
