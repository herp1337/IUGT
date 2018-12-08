# coding: utf8
#!usr/bin/python2
import argparse,urllib,urllib2
import json,re,sys,time
### Warna
N = '\033[0m'
W = '\033[1;37m'
B = '\033[1;34m'
M = '\033[1;35m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
I = '\033[1;3m'
LC = '\033[1;96m' 
########
def tulis(arg,string):
	print "%s(%s%s%s): %s%s"%(G,Y,arg,G,W,string)
def animasi():
	m=0
	print "%s--+--+--+"%(C)
	try:
		conn=urllib2.urlopen("http://google.com")
	except urllib2.URLError as e:
		tulis("INFO","Internet Problem")
		sys.exit()
	while m < 101:
		time.sleep(0.01)
		sys.stdout.write("\r%s(%sINFO%s) %sFetching Information %s%s"%(C,Y,C,W,R,m))
		sys.stdout.flush()
		m += 1
	print "\n%s--+--+--+"%(C)
#######
parser=argparse.ArgumentParser(description="%sInformation User Github%s By HeroBrinePE"%(G,N),epilog="%sFollow My Github:%s herp1337"%(C,N))
parser.add_argument("--info",help="Show Information Of A Given User")
parser.add_argument("--followers",help="Show List Followers Of A Given User")
parser.add_argument("--following",help="Show List Following Account Of A Given User")
parser.add_argument("--repos",help="Show List Repository Of A Given User")
parser.add_argument("--starred",help="Show Starred Repos Of A Given User")
parser.add_argument("--gists",help="Show List Gists Of A Given User")
parser.add_argument("--site",help="Get Site Powered By Github Io Of A Given User")
parser.add_argument("--events",help="Show Retreived Events Of A Given User")
argumen=parser.parse_args()
if argumen.info:
	animasi()
	try:
		array=urllib2.urlopen("https://api.github.com/users/"+argumen.info).read()
		data=json.loads(array)
		tulis("ID",data["id"])
		tulis("NODE",data["node_id"])
		tulis("LOGIN",data["login"])
		tulis("BLOG",data["blog"])
		tulis("TYPE",data["type"])
		tulis("SITE_ADMIN",data["site_admin"])
		tulis("FOLLOWER",data["followers"])
		tulis("FOLLOWING",data["following"])
		tulis("LOCATION",data["location"])
		tulis("REPOSITORY",data["public_repos"])
		tulis("GIST",data["public_gists"])
		tulis("ICO",data["avatar_url"])
		tulis("BIO",data["bio"])
		tulis("EMAIL",data["email"])
		tulis("TIME",data["created_at"]+" => "+data["updated_at"])
	except urllib2.HTTPError:
		tulis("INFO","Given User Not Found")
if argumen.followers:
	animasi()
	try:
		array=urllib2.urlopen("https://api.github.com/users/%s/followers"%(argumen.followers)).read()
		data=json.loads(array)
		i=0
		while i < len(data):
			tulis(data[i]["id"],data[i]["login"])
			tulis("LINK",data[i]["html_url"])
			print "%s----------------"%(G)
			i += 1
	except urllib2.HTTPError:
		tulis("INFO","Given User No Found")
if argumen.following:
	animasi()
	try:
		array=urllib2.urlopen("https://api.github.com/users/%s/following"%(argumen.following)).read()
		data=json.loads(array)
		i=0
		while i < len(data):
			tulis(data[i]["id"],data[i]["login"])
			tulis("LINK",data[i]["html_url"])
			print "%s----------------"%(G)
			i += 1
	except urllib2.HTTPError:
		tulis("INFO","Given User No Found")
if argumen.repos:
	animasi()
	try:
		array=urllib2.urlopen("https://api.github.com/users/%s/repos"%(argumen.repos)).read()
		data=json.loads(array)
		i=0
		while i < len(data):
			tulis(data[i]["id"],data[i]["full_name"])
			tulis("DESC",data[i]["description"])
			tulis("LANG",data[i]["language"])
			tulis("FORK",data[i]["fork"])
			tulis("FORKS_COUNT",data[i]["forks_count"])
			if data[i]["license"] != None:
				tulis("LICENSE",data[i]["license"]["name"])
			tulis("LINK",data[i]["owner"]["html_url"])
			print "%s----------------"%(G)
			i += 1
	except urllib2.HTTPError:
		tulis("INFO","Given User No Found")
if argumen.starred:
	animasi()
	try:
		array=urllib2.urlopen("https://api.github.com/users/%s/starred"%(argumen.starred)).read()
		data=json.loads(array)
		i=0
		while i < len(data):
			tulis(data[i]["id"],data[i]["full_name"])
			tulis("DESC",data[i]["description"])
			tulis("LINK",data[i]["html_url"])
			print "%s----------------"%(G)
			i += 1
	except urllib2.HTTPError:
		tulis("INFO","Given User No Found")
if argumen.gists:
	animasi()
	try:
		array=urllib2.urlopen("https://api.github.com/users/%s/gists"%(argumen.gists)).read()
		data=json.loads(array)
		if len(data) < 1:
			tulis("INFO","Given User No Found")
			sys.exit()
		i=0
		key=""
		while i < len(data):
			for nama in data[i]["files"]:
				tulis(data[i]["id"],nama)
				key=nama
			tulis("RAW",data[i]["files"][key]["raw_url"])
			tulis("SIZE",str(data[i]["files"][key]["size"])+" KB")
			tulis("TIME",data[i]["created_at"]+" => "+data[i]["updated_at"])
			tulis("DESC",data[i]["description"])
			tulis("LINK",data[i]["html_url"])
			print "%s----------------"%(G)
			i += 1
	except urllib2.HTTPError:
		tulis("INFO","Given User No Found")
if argumen.site:
	animasi()
	try:
		array=urllib2.urlopen("https://api.github.com/users/%s/repos"%(argumen.site)).read()
		data=json.loads(array)
		i=0
		while i < len(data):
			if ".github.io" in data[i]["full_name"]:
				tulis("SITE","http://"+data[i]["name"])
				f=urllib.urlopen("http://"+data[i]["name"])
				tulis("STATUS",f.getcode())				
				sys.exit()
			i += 1
	except urllib2.HTTPError:
		tulis("INFO","Given User No Found")
if argumen.events:
	animasi()
	try:
		array=urllib2.urlopen("https://api.github.com/users/%s/received_events"%(argumen.events)).read()
		data=json.loads(array)
		i=0
		while i < len(data):
			tulis("ACTOR",data[i]["actor"]["login"])
			tulis("ID",data[i]["id"])
			tulis("TYPE",data[i]["type"])
			print "%s----------------"%(G)
			i += 1
	except urllib2.HTTPError:
		tulis("INFO","Given User No Found")