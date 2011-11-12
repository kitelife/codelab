<?php
if($_FILES['article']['error']>0)
{
	echo 'Problem: ';
	switch($_FILES['article']['error'])
	{
		case 1: 
			echo 'File exceeded upload_max_filesize';
			break;
		case 2:
			echo 'File exceeded max_file_size';
			break;
		case 3:
			echo 'File only partially uploaded';
			break;
		case 4:
			echo 'No file uploaded';
			break;

	}
	exit;
}

// put the file where we'd like it
$upfile = $_SERVER['DOCUMENT_ROOT'].'miniblog/articles/'.$_FILES['article']['name'];
if(is_uploaded_file($_FILES['article']['tmp_name']))
{
	if(!move_uploaded_file($_FILES['article']['tmp_name'], $upfile))
	{
		echo 'Problem: Could not move file to destination directory!';
		exit;
	}
}
else
{
	echo 'Problem: possible file upload attack. Filename: ';
	echo $_FILES['article']['name'];
	exit;
}
$fileNamearray = explode(".",$_FILES['article']['name']);
$fileName=$fileNamearray[0];
@$db = new mysqli('localhost','root','','miniblog');
if(mysqli_connect_errno())
{
	echo 'Error: Could not connect to database!';
	exit;
}
$date = date('Y-m-d H:i');
if(!get_magic_quotes_gpc())
{
	$fileName=addslashes($fileName);
	$date=addslashes($date);
}

echo $fileName.'<br />';
echo $date.'<br />';
$sql = "insert into articles(dateposted, articleTitle)values('$date','$fileName')";
$result=$db->query($sql);
if($result){
	echo 'File uploaded successfully<br />';
}
else
{
	echo 'Error-> File uploaded failed!';
}
$db->close();
?>
