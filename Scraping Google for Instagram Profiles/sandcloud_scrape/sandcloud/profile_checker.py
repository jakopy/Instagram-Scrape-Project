with open("instagram_urls.txt", "r") as f:
    data = f.read().splitlines()

import requests
for url in data:
    print url
    r = requests.get(url)
    profile = url.split("//www.instagram.com/")[1]
    
    data= r.text
    try:
        followers = data.split('followed_by": {"count": ')[1].split("}")[0]
        print followers
    except Exception as e:
        print "0"

##from bs4 import BeautifulSoup
##soup = BeautifulSoup(data, 'html.parser')
##print soup.prettify()
