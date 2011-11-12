<?php
require_once('config.php');
require_once('view_functions.php');
session_start();
do_html_header($title);
display_articles_list();
if(!isset($_SESSION['valid_user']))
{
	echo '<br /><br /><center><div font="5">';
	echo '<a href="login.php">Login</a>';
	echo '</div></center>';
}
else
{
	echo '<br /><br /><center><div font="5">';
	echo '<a href="console.php">console</a>&nbsp&nbsp';
	echo '<a href="logout.php">Logout</a>';
	echo '</div></center>';
}
do_html_footer();
?>
