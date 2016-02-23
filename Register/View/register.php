<?php
session_start();
if(isset($_SESSION['ID'])!="")
{
	header("Location: home.php");
}
include_once '../Controller/DBConnection/DBConnectionController.php';

if(isset($_POST['btn-signup']))
{
	$fname = mysql_real_escape_string($_POST['fname']);
	$lname = mysql_real_escape_string($_POST['lname']);
	$CNO = mysql_real_escape_string($_POST['CNO']);
	$email = mysql_real_escape_string($_POST['email']);
	$address = mysql_real_escape_string($_POST['address']);
	$upass = md5(mysql_real_escape_string($_POST['pass']));
	
	$fname	= trim($fname);
	$lname 	= trim($lname);
	$CNO	= trim($CNO);
	$email	= trim($email);
	$address= trim($address);
	$upass	= trim($upass);
	
	// email exist or not
	$query = "SELECT email FROM s_user WHERE email='$email'";
	$result = mysql_query($query);
	
	$count = mysql_num_rows($result); // if email not found then register
	
	if($count == 0){
		
		if(mysql_query("INSERT INTO s_user(firstname, lastname, contactno, email, address, password	) VALUES('$fname','$lname','$CNO','$email','$address','$upass')"))
		{
			?>
			<script>alert('successfully registered ');</script>
			<?php
			header("Location: index.php");
			
		}
		else
		{
			?>
			<script>alert('error while registering you...');</script>
			<?php
		}		
	}
	else{
			?>
			<script>alert('Sorry Email ID already taken ...');</script>
			<?php
	}
	
}
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Registration</title>
<link rel="stylesheet" href="../css/style.css" type="text/css" />

</head>
<body>
<center>
<div id="login-form">
<form method="post">
<table align="center" width="56%" border="0">

<tr>
<td><input type="text" name="fname" placeholder="Your First Name" required /></td>
</tr>
<tr>
<td><input type="text" name="lname" placeholder="Your Last Name" required /></td>
</tr>
<tr>
<td><input type="email" name="email" placeholder="Your Email" required /></td>
</tr>
<tr>
<td><input type="password" name="pass" placeholder="Your Password" required /></td>
</tr>
<tr>
<td><input type="text" name="CNO" placeholder="Your Contact No" required /></td>
</tr>
<tr>
<td><input type="text" name="address" placeholder="Your Address" /></td>
</tr>
<tr>
<td><button type="submit" name="btn-signup">Sign Me Up</button></td>
</tr>
<tr>
<td><a href="index.php">Sign In Here</a></td>
</tr>
</table>
</form>
</div>
</center>
</body>
</html>