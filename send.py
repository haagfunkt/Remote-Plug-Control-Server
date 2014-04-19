#!/usr/bin/env python
import sys
import urllib2
import time
import os
from time import sleep
import sqlite3 as lite

#sys.argv[0] # this is the file name
#sys.argv[1] # this is the dip code	input in browser as string: dip="10010 2"
#sys.argv[2] # this is the state	input in browser:	    state=on
#sys.argv[3] # this is the time		input in browser:	    time=5
#sys.argv[n] # 
#example URL: 192.168.1.111/mfi.php?dip="10000 3"&state=off&time=5

php_dip=sys.argv[1]
php_state=sys.argv[2]
php_time=sys.argv[3]

#switch plug on or off ?
if php_state == "on":
    state = 1
    
elif php_state == "off":
    state = 0

#building the send command together
comm="send %s %s" %(php_dip, state)

#initialize timer if set
wait_time = float(php_time)
sleep(wait_time)

#run switch command for plug
for l in range(5):
	os.system("sudo /home/pi/raspberry-remote/%s" %comm)
	
################ Refresh State in SQL ########################
con = lite.connect('/home/pi/Steckdosen.db')			#Connect to SQL Database				
with con:
	cur = con.cursor()
	#cur.execute("DROP TABLE IF EXISTS plugs")
	#cur.execute("CREATE TABLE plugs(name TEXT, address TEXT, state TEXT)")
	cur.execute("UPDATE plugs SET state=? WHERE address=?", (state, php_dip))
	#cur.execute("INSERT INTO plugs VALUES(?, ?, ?)", (NAME,ADDRESS,STATE))		
		
	con.close
