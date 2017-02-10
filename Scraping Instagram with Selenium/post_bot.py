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
##                        print "video likes: " + str(likenum.text)

            elif number != 1: # Click and parse
                url_before = driver.current_url
                try:
                    likenum = driver.find_element_by_class_name(CSS_LIKES)
                    video= False
                    likenum = likenum.text
                except Exception as e:
                    video = True
                    viewsclicker = driver.find_element_by_class_name("_9jphp")
                    viewsclicker.click()
                    likenum = driver.find_element_by_class_name(CSS_VIDEO_LIKES)
##                    print "video likes: " + str(likenum.text)
                    likenum = str(likenum.text)
                    driver.execute_script("window.history.go(-1)")
                    driver.execute_script("window.history.go(1)")


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
##                        for i in clickablecontent:
##                            print i.text
                    
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
##                            for i in clickablecontent:
##                                print i.text
                    post_time_stamp = driver.find_element_by_class_name("_379kp")
                    post_time_stamp = post_time_stamp.get_attribute("datetime")
                    post_id = post_time_stamp
                    tags = []
                    users = []
                    poster = clickablecontent[0].text
                    for i in clickablecontent:
                        if "#" in i.text:
                            tags.append(i.text)
                        if "@" in i.text:
                            users.append(i.text)
                    post_data[post_id]=[poster,likenum,video,tags,users]

##                    current_profile
##                    def post_data_adder(post_data,current_profile):
##                        grab_current_cache
##                        #{profilename:[last_updated,pswd,followers,following,posts],profilename:[pswd,profphoto,hashtags,posts,followers,following]
##                        #post_bank = {post_id:[like_count,video?,hashtags,posters_comments]}
##                        
##                        with open("data/" + "database.txt") as f:
##                            current_data = f.readlines()
##                            for profiledata in current_data:
##                                profilename = current_data.split(",")[0]
##                                if current_profile in current_data:
##                                    posts_bank = current_data.split(",")[4]
##                                    posts_bank_count = len(posts_bank)
####                                pswd = current_data.split(",")[1]
####                                followers = current_data.split(",")[2]
####                                following = current_data.split(",")[3]
####                                posts_bank = current_data.split(",")[4]
####                                posts_bank_count = len(posts_bank)
##                        
##                        for post_ids in posts_bank:
##                            db_time_stamps = post_ids.split("_")[1]
##
##                        #check to see if post in database
##                            
##                        if post_time_stamp not in db_time_stamps:
##                            #add new post instance
##                            post_number = posts_bank_count + 1
##                            post_id = post_number + "_" + post_time_stamp
##                            
##                        #current posts in bank
##                        comment_list_in_cache = []
##                        for post_id in post_data:
##                            info = post_data[post_id]
##                            comment_list_in_cache.append(info[2])
##                        if posters_comment not in comment_list_in_cache:
##                            newpost_id = uuid.uuid4()
                
                driver.find_element_by_css_selector(CSS_RIGHT_ARROW).click()
                # Wait until the page has loaded
                WebDriverWait(driver, 10).until(
                    url_change(url_before)
                )
            captions.append(parse_caption())
        return post_data
    post_data = Post_Bot(driver,rules,current_profile)
    return post_data


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

##from log_bot import log_in
driver = webdriver.Firefox()
##log_in("imagograzm","Baijo77O",driver).run()


likeboundry = (50000,100000000)
withinlikeboudry = False
gethashtags = True
hashtags = [gethashtags,withinlikeboudry]
rules = ["none",likeboundry,hashtags]
post_data = scrapeposts("dogsofinstagram",15,rules)

for post in post_data:
    post_content = post_data[post]
    print post
    print post_content
