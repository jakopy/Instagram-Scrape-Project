###########################
#PROGRAM CODE
###########################

def LOGIN(user,pswd):
    driver.get('https://www.instagram.com/accounts/login')
    time.sleep(5)
    dom = driver.find_element_by_xpath('//*')
    username = dom.find_element_by_name('username')
    password = dom.find_element_by_name('password')
    login_button = dom.find_element_by_xpath('//*[@class="_aj7mu _taytv _ki5uo _o0442"]')
    username.clear()
    password.clear()
    username.send_keys(user)
    password.send_keys(pswd)
    time.sleep(5)
    login_button.click()
    time.sleep(5)
    return driver

def searchbarcrawl(searchterm):
    driver.get("https://instagram.com")
    searchbox = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Search']")
        )
    )
    searchbox.send_keys(searchterm)
    time.sleep(5)
    hreffind = driver.find_elements_by_class_name("_k2vj6")
    profiles = []
    tags = []
    data = {'tags':[],'profiles':[]}
    for i in hreffind:
        stuff = i.get_attribute("href")
        if "tags" in stuff:
            tagprof = stuff.split("/")[5]
            tags.append(tagprof)
            data['tags'].append(tagprof)
        else:
            prof = stuff.split("/")[3]
            profiles.append(prof)
            data['profiles'].append(prof)
    return data

def profilefollowercrawl(profile,numfollowers,allfollowers):
    url = "https://instagram.com/" + profile
    driver.get(url)
    CSS_FOLLOWERS = "a[href='/instagram/followers/']"
    FOLLOWER_PATH = "//div[contains(text(), 'Followers')]"
    FOLLOW_ELE = CSS_FOLLOWERS
    
    FOLLOW_ELE = CSS_FOLLOWERS
    FOLLOW_PATH = FOLLOWER_PATH
    def mkformat(number):
        if "m" in number:
            number = number.replace("m","")
            if "." in number:
                number = int(number.replace(".",""))*100000
                print "inside of mkformat here"
                return number
            else:
                number = int(number)*1000000
                return number
        if "k" in number:
            number = number.replace("k","")
            if "." in number:
                number = int(number.replace(".","")+ "00")
                return number
            else:
                number = int(number + "000")
                return number
        if "," in number:
            number = int(number.replace(",",""))
            return number
    try:
        driver.implicitly_wait(10)
        follow_ele = driver.find_element_by_xpath("//a/span")
        allfollowernumber = follow_ele.text
        allfollowernumber = mkformat(allfollowernumber)
        follow_ele.click()
    except Exception as e:
        print "test1 failure"
        try:
            postsfollow_ing = driver.find_elements_by_class_name("_bkw5z")
            number = postsfollow_ing[1].text
            number = mkformat(number)
            allfollowernumber = number
            postsfollow_ing[1].click()
        except Exception as e:
            print "test 2 failed"
    #follow element clicked
    time.sleep(1)
    title = driver.find_element_by_xpath(FOLLOW_PATH)
    List = title.find_element_by_xpath('..').find_element_by_tag_name('ul')
    ##print "find list"
    List.click()
    cur_follow_num = len(List.find_elements_by_xpath('*'))
    
    selfnumber = numfollowers
    if allfollowers == True:
        selfnumber = allfollowernumber
        
    if selfnumber > cur_follow_num:
        element = List.find_elements_by_xpath('*')[-1]

        while len(List.find_elements_by_xpath('*')) < selfnumber:
            element.send_keys(Keys.PAGE_DOWN)

        cur_follow_num = len(List.find_elements_by_xpath('*'))
        for _ in range(2*(selfnumber - cur_follow_num)/10):
            element.send_keys(Keys.PAGE_DOWN)

    followers =  []
    for ele in List.find_elements_by_xpath('*')[:selfnumber]:
        followers.append(ele.text.split('\n')[0])
        
    return followers

def scrapeposts(profile,photocrawlnumber,rules):
    current_profile = profile
    photocrawlnumber += 1
    url = "http://instagram.com/" + profile
    driver.get(url)

    number = photocrawlnumber
    
    def LOADPOSTS(number):
        CSS_LOAD_MORE = "a._oidfu"
        SCROLL_UP   = "window.scrollTo(0, 0);"
        SCROLL_DOWN = "window.scrollTo(0, document.body.scrollHeight);"
        driver.execute_script(SCROLL_DOWN)
        loadmore = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, CSS_LOAD_MORE))
        )
        loadmore.click()

        num_to_scroll = (number - 12)/12 + 1
        for _ in range(num_to_scroll):
            driver.execute_script(SCROLL_DOWN)
            time.sleep(0.05)
            driver.execute_script(SCROLL_UP)
            time.sleep(0.05)

        encased_photo_links = re.finditer(r'src="([https]+:...[\/\w \.-]*..[\/\w \.-]*'
                            r'..[\/\w \.-]*..[\/\w \.-].jpg)', driver.page_source)
        photo_links = [ m.group(1) for m in encased_photo_links ]
        
    LOADPOSTS(number)

    def parse_caption():
        TIME_TO_CAPTION_PATH = "../../following-sibling::ul/*/*/span"
        time = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.TAG_NAME, "time"))
        )
        try:
            caption = time.find_element_by_xpath(TIME_TO_CAPTION_PATH).text
        except NoSuchElementException: # Forbidden
            caption = ""

        return caption

    def Post_Bot(driver,rules,current_profile):
        #RULE MAKER
        lowerboundlikes = rules[1][0]
        upperboundlikes = rules[1][1]
        grab_hashtag_rule = rules[2][0]
        grab_hashtag_in_like_bound = rules[2][1]
        post_data ={}
        #posts = {post_id:[like_count,video?,hashtags,comments]}
        #we can use comments and like check as indicators if we already have a photo
        if rules[0] == "none":
            hitlike = False
            unlike = False
        else:
            if rules[0] == "like":
                hitlike = True
                unlike = False
            elif rules[0] == "unlike":
                unlike = True
                hitlike = False
            else:
                print "Invalid Rule Entry"
        #RULE MAKER END

        class url_change(object):
            def __init__(self, prev_url):
                self.prev_url = prev_url
            def __call__(self, driver):
                return self.prev_url != driver.current_url
        captions = []
        CSS_RIGHT_ARROW = "a[class='_de018 coreSpriteRightPaginationArrow']"

        CSS_LIKES = "_tf9x3"
        CSS_VIDEO_LIKES = "_mjnfc"
        for post_num in range(number):
            if post_num == 0: # Click on the first post
                driver.find_element_by_xpath("//a[contains(@class, '_8mlbc _vbtk2 _t5r8b')]").click()
                if number != 1: # If user has only one post
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,CSS_RIGHT_ARROW))
                    )
                    try:
                        likenum = driver.find_element_by_class_name(CSS_LIKES)
                        video = False
                    except Exception as e:
                        video = True
                        viewsclicker = driver.find_element_by_class_name("_9jphp")
                        viewsclicker.click()
                        likenum = driver.find_element_by_class_name(CSS_VIDEO_LIKES)
                        viewsclicker.click()
                        print "video likes: " + str(likenum.text)

            elif number != 1: # Click and parse
                url_before = driver.current_url
                try:
                    likenum = driver.find_element_by_class_name(CSS_LIKES)
                    video= False
                except Exception as e:
                    video = True
                    viewsclicker = driver.find_element_by_class_name("_9jphp")
                    viewsclicker.click()
                    likenum = driver.find_element_by_class_name(CSS_VIDEO_LIKES)
                    print "video likes: " + str(likenum.text)
                    driver.execute_script("window.history.go(-1)")
                    driver.execute_script("window.history.go(1)")

                likenum = likenum.text
                def likenumformater(likenum):
                    likenum = likenum.replace(" likes","")
                    if "k" in likenum:
                        newlike = likenum.split("k")[0]
                        if "." in newlike:
                            newlike = newlike.replace(".","")
                            likenum = str(newlike) + "00"
                        else:
                            likenum = str(newlike) + "000"
                            likenum = int(likenum)
                        likenum = int(likenum)
                    try:
                        if "," in likenum:
                            newlike = likenum.replace(",","")
                            likenum = int(newlike)
                        return likenum
                    except Exception as e:
                        "do nothing"
                    return likenum
                
                if grab_hashtag_rule == True:
                    if grab_hashtag_in_like_bound == False:
                        entire_comment_section = driver.find_element_by_css_selector("ul._mo9iw._123ym")
                        posters_comment = driver.find_element_by_class_name("_nk46a")
                        clickablecontent = posters_comment.find_elements_by_css_selector("a")
                        for i in clickablecontent:
                            print i.text
                    
                likenum = likenumformater(likenum)
                #posts = {post_id:[like_count,video?,hashtags,comments]}
                #likerangerule
                if upperboundlikes >= likenum >= lowerboundlikes:
                    #hitting the like button
                    if hitlike == True:
                        try:
                            likebutton = driver.find_element_by_css_selector("span._soakw.coreSpriteHeartOpen")
                            likebutton.click()
                        except Exception as e:
                            print "this already has a heart"
                    #Unliking the photo that has been liked
                    if unlike == True:
                        try:
                            thing = driver.find_element_by_class_name("_ebwb5")
                        except Exception as e:
                            print "Like heart failure"
                        try:
                            if "Like" not in thing.text:
                                alreadyliked = driver.find_element_by_css_selector("span._soakw.coreSpriteHeartFull")
                                alreadyliked.click()
                        except Exception as e:
                            print "UnLike heart Failure"
                            
                    if grab_hashtag_rule == True:
                        if grab_hashtag_in_like_bound == True:
                            entire_comment_section = driver.find_element_by_css_selector("ul._mo9iw._123ym")
                            posters_comment = driver.find_element_by_class_name("_nk46a")
                            clickablecontent = posters_comment.find_elements_by_css_selector("a")
                            
                            #posts = {post_id:[like_count,video?,hashtags,posters_comments]}
                            for i in clickablecontent:
                                print i.text
                    post_time_stamp = driver.find_element_by_class_name("_379kp")
                    post_time_stamp = post_time_stamp.get_attribute("datetime")
                    print post_time_stamp
                    post_id = post_time_stamp
                    current_profile
                    def post_data_adder(post_data,current_profile):
                        grab_current_cache
                        #{profilename:[last_updated,pswd,followers,following,posts],profilename:[pswd,profphoto,hashtags,posts,followers,following]
                        #post_bank = {post_id:[like_count,video?,hashtags,posters_comments]}
                        
                        with open("data/" + "database.txt") as f:
                            current_data = f.readlines()
                            for profiledata in current_data:
                                profilename = current_data.split(",")[0]
                                if current_profile in current_data:
                                    posts_bank = current_data.split(",")[4]
                                    posts_bank_count = len(posts_bank)
##                                pswd = current_data.split(",")[1]
##                                followers = current_data.split(",")[2]
##                                following = current_data.split(",")[3]
##                                posts_bank = current_data.split(",")[4]
##                                posts_bank_count = len(posts_bank)
                        
                        for post_ids in posts_bank:
                            db_time_stamps = post_ids.split("_")[1]

                        #check to see if post in database
                            
                        if post_time_stamp not in db_time_stamps:
                            #add new post instance
                            post_number = posts_bank_count + 1
                            post_id = post_number + "_" + post_time_stamp
                            
                        #current posts in bank
                        comment_list_in_cache = []
                        for post_id in post_data:
                            info = post_data[post_id]
                            comment_list_in_cache.append(info[2])
                        if posters_comment not in comment_list_in_cache:
                            newpost_id = uuid.uuid4()

                driver.find_element_by_css_selector(CSS_RIGHT_ARROW).click()
                # Wait until the page has loaded
                WebDriverWait(driver, 10).until(
                    url_change(url_before)
                )
            captions.append(parse_caption())
        return post_data
    Post_Bot(driver,rules,current_profile)

def profiledata(profile):
    url = "https://instagram.com/" + profile
    driver.get(url)
    driver.implicitly_wait(5)
    postsfollow_ing = driver.find_elements_by_class_name("_bkw5z")
##    print postsfollow_ing
    postnumber = postsfollow_ing[0]
    follownumber = postsfollow_ing[1]
    followingnumber = postsfollow_ing[2]
    print "posts: " + postnumber.text
    print "followers: " + follownumber.text
    print "following: " + followingnumber.text
    def profilepicgetter():
        image = driver.find_element_by_css_selector("img._8gpiy._r43r5")
        url = image.get_attribute("src")
        session = FuturesSession(max_workers=1)
        profile_image = [session.get(url)]
        profile_pic_response = profile_image[0].result()
        profile_pic = profile_pic_response.content    
        return profile_pic
    profile_pic = profilepicgetter()
    with open(profile + ".jpg",'wb') as f:
        f.write(profile_pic)

def CACHER(data,datatype):
    if datatype = "posts":
        #
        #followers = [follower_count,,,,,]
        #following = [following_count,,,,,]
        #posts = {post_count:54,post_id:[like_count,video?,hashtags,comments]}
        #{profilename:[last_updated,pswd,followers,following,posts],profilename:[pswd,profphoto,hashtags,posts,followers,following]
        for user in data
    #createdata
    #checkdataexist

import argparse
import codecs
import logging
import os
import pdb
import re
import time
import traceback
from urlparse import urljoin
import warnings

from requests_futures.sessions import FuturesSession
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException

############
### MAIN ###
############
    
##profiletoscrape = "intagram"
##numbertoscrape = "50"
##crawlphotos = True
###data set returned on photocrawl:> likes on photo must be above___ and below___
##photocrawlrules = [">50","<50000"]
##crawlfollowers = True
##gethashtagsfromphotos = True
##likeusers = False
##likeusersrules = [">50","<100"]

driver = webdriver.Firefox()
LOGIN('imagograzm','Baijo77O')

##data = searchbarcrawl("dogs")
#searchbar data return: {tags:[tag1,tag2],profile:[profile1,profile2]}
##count = 0
##for i in data['tags']:
##    count+=1
##print "total tags found: " + str(count)
##count2 = 0
##for i in data['profiles']:
##    count2+=1
##print "total profiles found: " + str(count2)
##print "total instances found: " + str(count + count2)

##profilefollowercrawl("dogsofinstagram",50,False)
#                   profile, numfollowers, crawl_all_followers

likeboundry = (50000,100000000)
withinlikeboudry = False
gethashtags = True
hashtags = [gethashtags,withinlikeboudry]
rules = ["none",likeboundry,hashtags]
###        none/like/unlike,(lowerboundlikes,upperboundlikes), grab hashtags
scrapeposts("dogsofinstagram",15,rules)
###       profile,numberofposts, rules

##profiledata("nectar")
