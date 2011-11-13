<?php
require_once('db_functions.php');

function do_html_header($title)
{
    //print an HTML header
?>
    <html>
		<head>
			<title><?php echo $title; ?></title>
		</head>
		<body>
		<img src="logo.png" alt="miniBlog logo" border=0
				align=left valign=bottom height = 55 width = 140 />
		<h1>&nbsp;Hacker's Whiteboard</h1>
		<hr />
<?php
}

function do_html_footer()
{
	// print an HTML footer
?>
	<center>
	<p>
	Powered By PHP<br />
	xiayf
	</p>
	</center>
	</body>
	</html>
<?php
}

function display_login_form()
{
?>
	<br /><br /><br />
	<form method="post" action="console.php">
	<table align='center' bgcolor='#94D0DF'>
		<tr>
			<td>UserName:</td>
			<td><input type='text' name='UserName'></td>
		</tr>
		<tr>
			<td>Password:</td>
			<td><input type='text' name='Password'></td>
		</tr>
		<tr>
			<td colspan=2 align='center'>
			<input type='submit' value='Login'>
			</td>
		</tr>
	</table>
	</form>	
<?php
}

function display_console_form()
{
?>
	<form enctype="multipart/form-data" action="upload.php" method="post">
	<center>
	<p>	
		<input type="hidden" name="MAX_FILE_SIZE" value="10000000">
		<input name="article" type="file">
		<input type="submit" value="Upload">
	</p>
	</center>
	</form>
<?php
}

function display_articles_list()
{
	$conn = new mysqli('localhost','root','','miniblog');
@	$result = $conn->query("select * from articles");
	if(!$result){
		echo 'Error: Problem when query!';
		exit;
	}
	if($result->num_rows == 0)
	{
		echo '<center><p>';
		echo 'Sorry, there is no article!';
		echo '</p></center>';
	}
	else{
		$num_articles = $result->num_rows;
		echo "<table align='center' border='0'>";
		for($i=0; $i<$num_articles; $i++)
		{
			$row = $result->fetch_assoc();
			echo '<tr>';
			echo '<td width=200>';
			echo "<font size='4' face='Verdana'>";
			echo htmlspecialchars(stripslashes($row['dateposted']));
			echo '</font></td>';
			echo "<td><font size='5' face='Verdana'><a href='./articles/";
			echo $row['articleTitle'];
			echo ".html' target='_blank'>";
			echo $row['articleTitle'];
			echo "</a></font></td>";
			echo '</tr>';
		}
		echo "</table>";
	}
			
}
?>
