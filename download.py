#!/bin/python3

import requests
import json
import urllib.request



#Making api call to /r/memes subreddit.

#These headers will make the request look like a firefox request, avoids 429 error
headers={
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"en-US,en;q=0.5",
"Connection":"keep-alive",
"DNT":"1",
"Host":"www.reddit.com",
"TE":"Trailers",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
}



memes_response = requests.get("https://www.reddit.com/r/memes.json",headers=headers)

#validating the response and extracting json
if memes_response.status_code == 200:
	memes_json = json.loads(memes_response.text)
elif memes_response.status_code == 429:
	print("!!!! Sending too many requests..... Reddit refused the connection, please try after a while !!!!")
	exit()
else:
	print(f"!!!! Error in connecting --- error code {memes_response.status_code} --- Please check your connection !!!!")
	exit()
	
#loading animation creator
def loader(iteration,total):
    percentage = 100 * iteration/float(total)
    
    print("["+"*"*int(percentage)+"-"*int(100-percentage)+"]"+str(int(percentage))+"%",end='\r')	



#going through all the posts in /r/memes homepage and checking for images

image_list=[]
for child in memes_json['data']['children']:
	if child['data']['post_hint'] == 'image':
		image_list.append(child['data']['url'])

done=0
total=len(image_list)
loader(done,total)

for url in image_list:
    urllib.request.urlretrieve(url,url.split('/')[-1])
    done+=1
    loader(done,total)
    
print()
    

  
  
  
