<?php

/************ URL ZUGRIFF *************/

$dip = $_GET["dip"];
$state = $_GET["state"];
$time = $_GET["time"];

echo $dip;
echo $state;
echo $time;

if ($time=="")
{
	 $time=0;
}
echo $time;


$temp = exec("sudo /var/www/send.py $dip $state $time");

echo "success";

/************* GUI ********************/
?> 
