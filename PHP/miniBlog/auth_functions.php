<?php
require_once('db_functions.php');

function login($UserName, $Password)
{
	//connect to db
@	$conn = new mysqli('localhost','root','','miniblog');
	if(mysqli_connect_errno())
	{
		echo 'Error:Could not connect to database;';
		exit;
	}
	// check if username is unique
	$conn->query("SET NAMES 'UTF8'");
	$sql='select * from users where username="'.$UserName.'" and password=sha1("'.$Password.'")';
	$result = $conn->query($sql);
	if(!$result)
	{
		echo "Could not connect!\n";
	}	
	if($result->num_rows > 0)
		return true;
	else
		throw new Exception('Could not log you in!');
}
?>
