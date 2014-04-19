<?php
 
/* Check which button was pressed */
if (isset($_POST['buttonA0'])) { shell_exec('sudo /home/pi/raspberry-remote/send 10010 1 0'); }
if (isset($_POST['buttonA1'])) { shell_exec('sudo /home/pi/raspberry-remote/send 10010 1 1'); }
 
if (isset($_POST['buttonB0'])) { shell_exec('sudo /home/pi/raspberry-remote/send 10010 2 0'); }
if (isset($_POST['buttonB1'])) { shell_exec('sudo /home/pi/raspberry-remote/send 10010 2 1'); }
 
if (isset($_POST['buttonC0'])) { shell_exec('sudo /home/pi/raspberry-remote/send 10010 3 0'); }
if (isset($_POST['buttonC1'])) { shell_exec('sudo /home/pi/raspberry-remote/send 10010 3 1'); }

	

 
$sysinfo = shell_exec('uname -nmor');
$systime = shell_exec('date');
 
?>
 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
       "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>

<h1>neue Steckdose anlegen</h1>

<form action="plugPHP.php" method="post">
  <p>name:<br><input name="name" type="text" size="30" maxlength="30"></p>
  <p>code:<br><input name="code" type="text" size="30" maxlength="40"></p>
  <input type="submit">
</form>
	


<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>RPi</title>
 
<style type="text/css">
body {
	background-color:#1b191a;
	background-image:url(bg.jpg);
	color: white;
	}
 
.wrapButtons {
	text-align:center;
	font-size:25px;
	font-family:verdana, sans-serif;
	}
.submitButton{
	text-align:left;
	font-size:25px;
	font-family:verdana, sans-serif;
	} 
.onButton, .offButton {
	width:200px;
	height:100px;
	margin:-10px 10px 0px 10px; /* o-r-u-l */
	color:white;
	background-color:#53bc41;
	border-radius:8px;
	font-size:50px;
	}
 
.offButton {
	background-color:#e40e12;
	}
</style>
 
<script type="text/javascript"></script>
</head>
<body>
 
<form action="" method="post">
    <div class="submitButton">
	<button class="submitButton" type="submit" name="buttonEnter">ENTER</button>
    </div>

	<div class="wrapButtons">
	<p>Steckdose A</p>
    	<button class="offButton" type="submit" name="buttonA0">Aus</button>
    	<button class="onButton" type="submit" name="buttonA1">Ein</button>
    </div>
 
    <div class="wrapButtons">
	<p>Steckdose B</p>
    	<button class="offButton" type="submit" name="buttonB0">Aus</button>
    	<button class="onButton" type="submit" name="buttonB1">Ein</button>
    </div>
 
    <div class="wrapButtons">
	<p>Steckdose C</p>
    	<button class="offButton" type="submit" name="buttonC0">Aus</button>
    	<button class="onButton" type="submit" name="buttonC1">Ein</button>
    </div>


</form>
 
<hr style="margin-top:35px;">
<p style="text-align:center;">System: <?php echo $sysinfo; ?> - Systemzeit: <?php echo $systime; ?></p>
 
</body>
</html>