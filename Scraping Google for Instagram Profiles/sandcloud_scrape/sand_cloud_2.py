search_term = "money"

import requests
from random import randint
import time
pagenumbers = ["0","100","200"]
all_urls = []
all_names = []
new_pages = []
for pages in pagenumbers:
    page = "https://www.google.com/search?q=site:instagram.com+%2B+"+search_term+"&num=100&biw=1536&bih=735&ei=7xySWOiBIIrLmwHZ0r2QDw&start="+pages+"&sa=N"
    r = requests.get(page)
    random_sleep = randint(5,7)
    time.sleep(random_sleep)
    data = r.text
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data, 'html.parser')

    h3s = soup.find_all('h3')

    profile_urls = []
    for item in h3s:
        long_url = item.a.get("href").replace("/url?q=","")
        short_url = long_url.split("&sa=")[0]
        if "/p/" not in short_url:
            if "google" not in short_url:
                if "l.insta" not in short_url:
                    if "preprod" not in short_url:
                        profile_urls.append(short_url)
        if "/p/" in short_url:
            if "l.insta" not in short_url:
                if "preprod" not in short_url:
                    if "%3Ftagged" not in short_url:
                        if "%3Ftaken-by%" in short_url:
                            short_url = short_url.split("%3Ftaken-by%")[0]
                        new_pages.append(short_url)
    
    for profile in profile_urls:
        if "explore" not in profile:
            all_urls.append(profile)
            profile_name = profile.split("instagram.com/")[1].split("/")[0]
            all_names.append(profile_name)
            
urls = []
for url in all_urls:
    if "%3F" in url:
        url = url.split("/%3F")[0]
    if "help" not in url:
        urls.append(url)
print "======================="
print "PEOPLE FOUND"
print "======================="
all_info = {}
for url in urls:
    if "preprod" not in url:
        if "https://www.instagram.com/" in url:
            name = url.split("https://www.instagram.com/")[1]
            name = name.replace("/","")
        if "www." not in url:
            print url
            name = url.split("https://instagram.com/")[1]
            name = name.replace("/","")
        r = requests.get(url)
        data= r.text
        json_data = data.split("window._sharedData = ")[1]
        json_data = json_data.split("</script>")[0]
##        print json_data
        json_formatted = json_data.split(" ")
        tagged_people = []
        for item in json_formatted:
            if "@" in item:
                if item != "@":
                    item = item.replace(",","")
                    tagged_person = item.replace("'","")
                    tagged_person = tagged_person.replace('"',"")

                    tagged_people.append(tagged_person)
        likes_found = json_data.split('likes": {"count": ')
        likesum = 0
        count = 0
        for like in likes_found:
            if count > 0:
                like_number = like.split("}}")[0]
                like_number = int(like_number)
                likesum += like_number
            count += 1
        average_likes = likesum/count

        try:
            followers = data.split('followed_by": {"count": ')[1].split("}")[0]
            followers = str(followers)
        except Exception as e:
            followers = "0"
        print "==============================="
        print "NAME: " + name
        print "FOLLOWERS: " + str(followers)
        print "AVERAGE LIKES: " + str(average_likes)
        print "URL: " + url
        print "TAGGED PEOPLE"
        for person in tagged_people:
            print person
        all_info[name]=[followers,url]

##from bs4 import BeautifulSoup
print "======================"
print "OTHER POSTS"
print "======================"
import json
import requests
count = 0
for new_url in new_pages:
    r = requests.get(new_url)
    data = r.text
    soup = BeautifulSoup(data,"html.parser")
    if "The link you followed may be broken, or the page may have been removed." not in data:
        if "See this Instagram photo by" in data:
            poster_likes = data.split("See this Instagram photo by ")[1]
            poster_likes = poster_likes.split('/>')[0]
        else:
            poster_likes = data.split("See this Instagram video by ")[1]
            poster_likes = poster_likes.split('/>')[0]
        poster_likes = poster_likes.replace('"',"")
        poster_likes = poster_likes.replace('" name="description"',"")
        poster_likes = poster_likes.replace("name=description","")
        jsondata = data.split("window._sharedData = ")[1]
        jsondata = jsondata.split("</script>")[0]
        jsonstring = jsondata
        json_formatted = jsonstring.split(" ")

        found_by_caption = []
        if "'caption': " in jsonstring:
            caption = jsonstring.split("'caption': ")[1]
        else:
            caption = jsonstring.split('"caption": ')[1]
        caption = caption.split(' "comments":')[0]
        tagged_people = caption.split(" ")
        for word in tagged_people:
            if "@" in word:
                tagged = word.replace(",","")
                tagged = tagged.replace("'","")
                tagged = tagged.replace('"',"")
                found_by_caption.append(tagged)
        not_found_by_caption = []
        for word in json_formatted:
            if "@" in word:
                tagged = word.replace(",","")
                tagged = tagged.replace("'","")
                tagged = tagged.replace('"',"")
                not_found_by_caption.append(tagged)
        print "======================"
        print new_url
        print "THE POSTER: " + poster_likes
        if len(found_by_caption) == 0:
            print "CAPTIONS: NO TAGGED PERSON FOUND IN CAPTION"
        else:
            print "CAPTIONS:"
            for person in found_by_caption:
                print person
        print "OTHERS FOUND:"
        for person in not_found_by_caption:
            print person

                
