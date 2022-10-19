W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'
import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor
import requests,bs4,uuid,json,os,sys,random,datetime,time,re,subprocess
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit(' [×] Cant Install Rich Module, Try Manual Install (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
import base64
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from urllib.parse import quote
# UA LIST
#ugen2=open('frec.txt','r').read().splitlines()
#ugen=open('m.txt','r').read().splitlines()
id,id2,loop,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,[],[],[],[],[],[],[],[]
cp = 0
ok = []
try:
	os.mkdir('/sdcard/')
except:pass
# COLORS
x = '\33[m' 
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m' 
u = '\033[95m' 
K = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m' 
# Converter 
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'Agustus','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'Agustus','09':'September','10':'October','11':'November','12':'December'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
# CLEAR
def clear():
	os.system('clear')
# BACK
def back():
	login()

ahsan="C~O~D~E~"
imt="-2.0=="
ak="K~E~Y~"
myid=uuid.uuid4().hex[:10].upper()
try:
	key1 = open('/data/data/com.termux/files/usr/bin/.mrkausar-cov', 'r').read()
except:
	kok=open('/data/data/com.termux/files/usr/bin/.mrkausar-cov', 'w')
	kok.write(myid+imt)
	kok.close()

############### #LOGO############## ## 


logo = ("""
--------/$$      /$$ /$$$$$$ /$$   /$$ /$$   /$$  /$$$$$$  /$$$$$$$$\033[1;91m
-------| $$$    /$$$|_  $$_/| $$$ | $$| $$  | $$ /$$__  $$|_____ $$ \033[1;92m
-------| $$$$  /$$$$  | $$  | $$$$| $$| $$  | $$| $$  \ $$     /$$/ \033[1;93m
-------| $$ $$/$$ $$  | $$  | $$ $$ $$| $$$$$$$$| $$$$$$$$    /$$/ \033[1;94m 
-------| $$  $$$| $$  | $$  | $$  $$$$| $$__  $$| $$__  $$   /$$/ \033[1;95m
-------| $$\  $ | $$  | $$  | $$\  $$$| $$  | $$| $$  | $$  /$$/\033[1;96m
-------| $$ \/  | $$ /$$$$$$| $$ \  $$| $$  | $$| $$  | $$ /$$$$$$$$\033[1;97m
-------|__/     |__/|______/|__/  \__/|__/  |__/|__/  |__/|________/\033[1;98m""")

class Main:
  os.system('clear')
  import XYZ
  XYZ.login()


	
def Subscraption():
	key1=open('/data/data/com.termux/files/usr/bin/.mrkausar-cov', 'r').read()
	clear()
	print(logo)
	r1=requests.get("https://github.com/maminhaz60/minhu2.0/blob/main/Approved.txt").text
	if key1 in r1:
		os.system('clear')
		print(logo)
		Main()
	else:
		os.system("clear")
		print(logo)
		print("\t \033[1;32m First Get Approvel\033[1;37m ")
		time.sleep(1)
		os.system("clear")
		print(logo)
		print ("")
		print(" \033[1;35mYOU NEED GET APPROVED FIRST\033[1;37m\n")
		print ("")
		print(" Your Key is Not Approved ")
		print("")
		print(" Copy And Send Key To Admin")
		print ("")
		print (" Your Key : \033[1;91m"+ak+ahsan+key1)
		print ("\033[0m")
		name = input(" Your Name : ")
		print ("")
		input(" Press Enter To Buy This Tool↩️")
		time.sleep(3.5)
		tks = 'Dear%20Admin,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'+ak+ahsan+''+key1
		os.system('am start https://wa.me/+8801612408902?text=' + tks)
		Subscraption()        
Subscraption()

