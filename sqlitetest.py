# -*- coding:utf-8 -*-   
#获取并打印google首页的html  
import urllib.request
from bs4 import BeautifulSoup
import time
import json
from urllib.parse import urlparse
import os

def getdata(url='http://www.nufe.edu.cn'): 
	response=urllib.request.urlopen(url)  
	html=response.read()  
	print(html)
	bs = BeautifulSoup(html,"html.parser")
	print (bs)
	return bs

def getinfo(bs):
	la = bs.find_all('a')
	print (len(la))
	res = []
	for a in la:
		if len(a.text)>0 and a.get('href') and len(a.get('href'))>2:
			print (a)
			if a.get('href')[:4]=='http':
				print (a.text,a.get('href'))
				res.append(a.get('href'))
		break
	return res

def getallpages(url):
	bs = getdata(url)

def getname(url):
	dest_str  = urlparse(url)
	print (dest_str)
	print (dest_str.netloc)
	fname = dest_str.netloc+'.'+dest_str.path+'.json'
	fname = fname.replace('/','_')
	return fname

def save(url,res):
	with open(getname(url),'w') as f:
		json.dump(res,f)

def main():
	url = 'http://www.nufe.edu.cn'
	fname = getname(url)
	if os.path.exists(fname):
		with open(fname,'r') as f:
			res=json.load(f)
		print ('exists')
	else:
		bs = getdata()
		res = getinfo(bs)
		print (res)
		save(url,res)
	return
	for r in res:
		bs = getdata(r)
		print (r)
		res = getinfo(bs)
		print (r,len(res))
		save(r,res)
		time.sleep(2)
		break

if __name__ == '__main__':
	main()