class profile_bot():
    def __init__(self,users,driver):
        self.users = users
        self.driver = driver
    def run(self):
        users = self.users
        driver = self.driver
        data = {}
        for user in users:
            try:
                from selenium import webdriver
                from requests_futures.sessions import FuturesSession 
                import time
                url = "https://instagram.com/" + user
                driver.get(url)
                driver.implicitly_wait(5)
                postsfollow_ing = driver.find_elements_by_class_name("_bkw5z")
                postnumber = postsfollow_ing[0]
                follownumber = postsfollow_ing[1]
                followingnumber = postsfollow_ing[2]
                profiledescription = driver.find_element_by_class_name("_bugdy")
                profiledescription = profiledescription.text
            
                def numberformater(num):
                    if "k" in num:
                        newnum = num.split("k")[0]
                        if "." in newnum:
                            newnum = newnum.replace(".","")
                            num = str(newnum) + "00"
                        else:
                            num = str(newnum) + "000"
                            num = int(num)
                        num = int(num)
                        return num
                    if "m" in num:
                        newnum = num.split("m")[0]
                        if "." in newnum:
                            newnum = float(newnum)*1000000
                            num = int(newnum)
                        else:
                            newnum = int(newnum)*1000000
                            num = newnum
                        return num
                    try:
                        if "," in num:
                            newnum = num.replace(",","")
                            num = int(newnum)
                        return num
                    except Exception as e:
                        "do nothing"
                    return num
                follownumber = numberformater(follownumber.text)
                postnumber = numberformater(postnumber.text)
                followingnumber = numberformater(followingnumber.text)
                def unicode_to_string(item):
                    import unicodedata
                    newstring = unicodedata.normalize('NFKD', item).encode('ascii','ignore')
                    return newstring
                def profilepicgetter():
                    image = driver.find_element_by_css_selector("img._8gpiy._r43r5")
                    url = image.get_attribute("src")
                    session = FuturesSession(max_workers=1)
                    profile_image = [session.get(url)]
                    profile_pic_response = profile_image[0].result()
                    profile_pic = profile_pic_response.content
                    with open("profilepicdata/"+user + ".jpg",'wb') as f:
                        f.write(profile_pic)
                    return profile_pic
                profile_pic = profilepicgetter()
                user = unicode_to_string(user)
                profiledescription = unicode_to_string(profiledescription)
                profileinfo = [profiledescription,postnumber,follownumber,followingnumber]
                data[user]=profileinfo
            except Exception as e:
                "profile data DNE (does not exist)"
        return data

#main
from selenium import webdriver
driver = webdriver.Firefox()
profile = "nectar"
profiletorun = profile_bot(profile,driver)
data = profiletorun.run()
for i in data:
    print i
