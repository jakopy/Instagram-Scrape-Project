from Downloader import Downloader2
D = Downloader2()
searchterm = "superheros"
html = D("https://www.instagram.com/web/search/topsearch/?context=blended&query=" + searchterm +"&rank_token=0.4302789341207505")

##import time
##time.sleep(5)
import json
data = json.loads(html)

##https://www.instagram.com/ajax
##https://www.instagram.com/web/search/topsearch/?context=blended&query=c&rank_token=0.3267988496143941
##for i in data:
##    print i
userinfo = {}
for i in data['users']:
    username = i['user']['username']
    followers = i['user']['follower_count']
    profile_pic = i['user']['profile_pic_url']
    privacy_check = i['user']['is_private']
    if username not in userinfo.keys():
        userinfo[username]=[followers,profile_pic,privacy_check]
    
for i in userinfo:
    print i
