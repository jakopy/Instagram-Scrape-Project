# ENTER YOUR SEARCH TERM HERE
search_term = "sandcloud+towels"

import requests
from bs4 import BeautifulSoup

pagenumbers = ["0","100","200"]
all_urls = []
all_names = []
for pages in pagenumbers:
    page = "https://www.google.com/search?q=site:instagram.com+%2B+"+search_term+"&num=100&biw=1536&bih=735&ei=skNxWJu0A4PJmwG-l7PACA&start="+pages+"&sa=N"
    r = requests.get(page)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')

    h3s = soup.find_all('h3')

    profile_urls = []
    for item in h3s:
        long_url = item.a.get("href").replace("/url?q=","")
        short_url = long_url.split("&sa=")[0]
        if "/p/" not in short_url:
            if "google" not in short_url:
                if "l.insta" not in short_url:
                    profile_urls.append(short_url)
    
    for profile in profile_urls:
        if "explore" not in profile:
            all_urls.append(profile)
            profile_name = profile.split("instagram.com/")[1].split("/")[0]
            all_names.append(profile_name)
urls = []
for url in all_urls:
    if "%3F" in url:
        url = url.split("/%3F")[0]
    urls.append(url)

for url in urls:
    if "preprod" not in url:
        name = url.split("https://www.instagram.com/")[1]
        name = name.replace("/","")
        r = requests.get(url)
        data= r.text
        try:
            followers = data.split('followed_by": {"count": ')[1].split("}")[0]
            print "FOLLOWERS: " +str(followers)
        except Exception as e:
            followers = "0"
        print "NAME: " + name
        print "FOLLOWERS: " + str(followers)
        print "URL: " + url
        
