<?php
session_start();
include_once '../Controller/DBConnection/DBConnectionController.php';

if(!isset($_SESSION['ID']))
{
	header("Location: index.php");
}
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Welcome</title>
<link rel="stylesheet" href="../css/style.css" type="text/css" />
</head>
<body>
<div id="header">
	<div id="left">
    <!--label></label-->
    </div>
    <div id="right">
    	<div id="content">
        	hi <?php echo $_SESSION['firstname'] . " " . $_SESSION['lastname']; ?>&nbsp;<a href="../Controller/logout.php?logout">Sign Out</a>
        </div>
    </div>
</div>

<div id="body">

</div>

</body>
</html>