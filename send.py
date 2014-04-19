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
#sys.argv[4] # this is the group 
#example URL: 192.168.1.111/mfi.php?dip="10000 3"&state=off&time=5

con = lite.connect('/home/pi/Steckdosen.db')			#Connect to SQL Database

php_dip=sys.argv[1]
php_state=sys.argv[2]
php_time=sys.argv[3]
php_group=sys.argv[4]

print php_dip
ret_state=100
count=1
i=0

#switch plug on or off ?
if php_state == "on":
    state = 1
    
elif php_state == "off":
    state = 0

#group on / off
if php_group != "no_group":
     with con:
	cur = con.cursor()
	cur.execute("SELECT address FROM plugs WHERE category=?", (php_group,))
	ret_address = cur.fetchall()
	print ret_address
	print len(ret_address)
	con.close
	count = len(ret_address)
	print "KKAKAKAKK"
	if count == 1:
		php_dip = ret_address[0]
		php_dip = php_dip[0]

#all on 
if php_dip == "all on":
     with con:
	cur = con.cursor()
	cur.execute("SELECT address FROM plugs WHERE state=0")
	ret_address = cur.fetchall()
	print ret_address
	print len(ret_address)
	con.close
	count = len(ret_address)
	if count == 1:
		php_dip = ret_address[0]
		php_dip = php_dip[0]
	state = 1
	php_state=state
#all off
if php_dip == "all off":
     with con:
	cur = con.cursor()
	cur.execute("SELECT address FROM plugs WHERE state=1")
	ret_address = cur.fetchall()
	print ret_address
	print len(ret_address)
	con.close
	count = len(ret_address)
	if count == 1:
		php_dip = ret_address[0]
		php_dip = php_dip[0]
	state = 0
	php_state=state
	
	
#get address from SQL if name is committed
php_dip_first_letter = php_dip[:1]
if php_dip[:1] != "0" and php_dip[:1] != "1" and php_dip != "all on" and php_dip != "all off":
     with con:
	cur = con.cursor()
	cur.execute("SELECT address FROM plugs WHERE name=?", (php_dip,))
	ret_address = cur.fetchone()
	con.close
	php_dip=ret_address[0]


#get state from SQL
if php_state == "toggle":
    with con:
	cur = con.cursor()
	cur.execute("SELECT state FROM plugs WHERE address=?", (php_dip,))
	ret_state = cur.fetchone()
	con.close
	ret_state=ret_state[0]

#invert state
if ret_state == "0":
    state = "1"
elif ret_state == "1":
    state = "0"

#initialize timer if set
wait_time = float(php_time)
sleep(wait_time)

for i in range(count):
	print i
	if count > 1:
		php_dip=ret_address[i]
		php_dip=php_dip[0]
		print php_dip
	#building the send command together
	comm="send %s %s" %(php_dip, state)

	#run switch command for plug
	for l in range(5):
		os.system("sudo /home/pi/raspberry-remote/%s" %comm)	
################### Refresh State in SQL ########################
	with con:
		cur = con.cursor()####
		#cur.execute("DROP TABLE IF EXISTS plugs")
		#cur.execute("CREATE TABLE plugs(name TEXT, address TEXT, state TEXT, group TEXT)")
		cur.execute("UPDATE plugs SET state=? WHERE address=?", (state, php_dip))####
		#cur.execute("INSERT INTO plugs VALUES(?, ?, ?)", (NAME,ADDRESS,STATE))	
		#INSERT INTO plugs VALUES('C','10010 3','1','zimmer');	
		
		con.close


