import json
from urllib.request import urlopen


def fun1():
	print("Dear nice to meet you~")

def fun2():
	url = "https://gdata.youtube.com/feeds/api/standardfeeds/top_rated? alt=json" 
	response = urlopen(url) 
	contents = response.read() 
	text = contents.decode('utf8') 
	data = json.loads(text) 

	for video in data['feed']['entry'][0:6]:
		print(video['title']['$t']) 