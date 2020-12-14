import requests

def ToBeDownloadedLinks():
	download=[]
	f=open("to-be-downloaded.txt","r")
	for url in f:
		# ~ link.
		if(url=="\n"):
			continue
		if(url.endswith("\n")):
			url=url[:-1]
		download.append(url)
	return download

def isDownloadable(url):
	h=requests.head(url,allow_redirects=True)
	header=h.headers
	contentType=header.get('content-type')
	#print(url)
	if(contentType==None):
		return False
	if 'text' in contentType.lower():
		return False
	if 'html' in contentType.lower():
		return False
	return True
	
def startDownloading(toBeDownloaded):
	for url in toBeDownloaded:
		if(isDownloadable(url)==True):
			fileName=url.rsplit('/',1)[1]
			r=requests.get(url,allow_redirects=True)
			open(fileName,'wb').write(r.content)
			print(fileName,"is successfully downloaded")
		else:
			print("This url is not Downloadable",url)

def main():
	toBeDownloaded=ToBeDownloadedLinks()
	startDownloading(toBeDownloaded)


if __name__=="__main__":
	main()


