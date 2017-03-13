from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import Queue
import threading
import requests
import time
import os


def scrape_posts(user,photocrawlnumber):
    profile = user
    url = "http://instagram.com/" + profile
    driver.get(url)
    
    if photocrawlnumber == False:
        Number_of_posts = driver.find_element_by_css_selector("span._bkw5z")
        Number_of_posts = Number_of_posts.text
        Number_of_posts = Number_of_posts.replace(",","")
        Number_of_posts = int(Number_of_posts)
        photocrawlnumber = Number_of_posts
        print "NUMBER OF POSTS THAT CAN BE SCRAPED: " + str(Number_of_posts)
    else:
        photocrawlnumber += 1
    

    number = photocrawlnumber

    
    def LOADPOSTS(number):
        SCROLL_UP   = "window.scrollTo(0, 0);"
        SCROLL_DOWN = "window.scrollTo(0, document.body.scrollHeight);"
        driver.execute_script(SCROLL_DOWN)
        try:
            driver.find_element_by_css_selector("a._oidfu")
            CSS_LOAD_MORE = "a._oidfu"
        except Exception as e:
            CSS_LOAD_MORE = "a._8imhp._glz1g"
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
        
    LOADPOSTS(number)
    
    def scrape(number):
        tagged_people_urls = []
        CSS_RIGHT_ARROW = "a[class='_de018 coreSpriteRightPaginationArrow']"
        CSS_LIKES = "_tf9x3"
        CSS_VIDEO_LIKES = "_mjnfc"
                
        for post_num in range(number):
            if post_num == 0:
                #click on first post
                driver.find_element_by_xpath("//a[contains(@class, '_8mlbc _vbtk2 _t5r8b')]").click()            
            else:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,CSS_RIGHT_ARROW))
                )
                try:
                    WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,"span._tf9x3"))
                        )
                    likenum = driver.find_element_by_class_name(CSS_LIKES)
                    likenum = likenum.text
                    video = False
                except Exception as e:
                    try:
                        video = True
                        viewsclicker = driver.find_element_by_class_name("_9jphp")
                        viewsclicker.click()
                        likenum = driver.find_element_by_class_name(CSS_VIDEO_LIKES)
                        likenum = likenum.text
                        driver.execute_script("window.history.go(-1)")
                        driver.execute_script("window.history.go(1)")
                    except Exception as e:
                        print "nonnumerical likenumber found"
                try:
                    WebDriverWait(driver,5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,"div._ovg3g"))
                        )
                    driver.find_element_by_css_selector("div._ovg3g").click()
                    people_in_photo = driver.find_elements_by_css_selector("a._ofpcv")
                    current_tagged_length = len(tagged_people_urls)
                    for person in people_in_photo:
                        url = person.get_attribute("href")
##                        print "PERSON TAGGED IN PHOTO!!"
##                        print url
                        tagged_people_urls.append(url)
                        name = url.split("https://www.instagram.com/")[1]
                        name = name.replace("/","")
##                        print name
                    new_tagged_length = len(tagged_people_urls)
                    if new_tagged_length <= current_tagged_length or new_tagged_length == 0:
                        try:
                            r = requests.get(driver.current_url)
                            rdata = r.text
                            caption = rdata.split('"caption": "')[1]
                            caption = caption.split('", "comments":')[0]                        
                            words = caption.split(" ")
                            tagged_people = []
                            for word in words:
                                if "@" in word:
##                                    print word
                                    url = word.replace("@","")
                                    url = "https://www.instagram.com/"+url
                                    tagged_people_urls.append(url)
                        except Exception as e:
                            print "NO TAGGED PERSON IN PHOTO HERE!"
                except Exception as e:
                    "no tagged, no caption"
##                            print caption.text
##                print video
##                print likenum
##                print "========================================="
                #WHAT WE HAVE SO FAR: VIDEO?, LIKES, person in pic
                driver.find_element_by_css_selector(CSS_RIGHT_ARROW).click()
        return tagged_people_urls
    
    tagged_people_urls = scrape(number)
    
    return tagged_people_urls

class Downloader(threading.Thread):

    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            url = self.queue.get()
            self.download_file(url)
            self.queue.task_done()

    def download_file(self, url):
        profile = url.split("https://www.instagram.com")[0]
        filename = "data/"+profile + ".txt"
        url = url.split(profile)[1]
        person_in_profile = url.split("//www.instagram.com/")[1]
        person_in_profile = person_in_profile.replace("/","")
        r = requests.get(url)
        data= r.text
        try:
            likes = data.split('"likes": {"count": ')
            likes = likes[1:len(likes)]
            like_sum = 0
            number_of_likes = 0
            for i in likes:
                likes_count = i.split('}}')[0]
##                print likes_count
                like_sum += int(likes_count)
                number_of_likes += 1
            average_likes = like_sum / number_of_likes
            average_likes = "average_likes: " + str(average_likes)
            person_in_profile
            url
            followers = "followers: " + data.split('followed_by": {"count": ')[1].split("}")[0]
            following = "following: " + data.split('"follows": {"count": ')[1].split("}")[0]
            try:
                post = "posts: " + data.split('"media": {"count": ')[1].split(",")[0]
            except Exception as e:
                post = "posts: " +data.split("Following, ")[1].split(" Posts")[0]
            data_found = True
        except Exception as e:
            message = "No data for " + person_in_profile
            data_found = False


        if data_found == True:
            with open(filename,'a') as f:
                f.write("\n"+person_in_profile+"\n")
                f.write(url+"\n")
                f.write(average_likes+"\n")
                f.write(followers+"\n")
                f.write(following+"\n")
                f.write(post+"\n")
                f.write("=============")
            f.close()
        else:
            with open(filename,'a') as f:
                f.write("\n"+message+"\n")
                f.write(url+"\n")
                f.write("=============")
            f.close()

def main(urls):
    queue = Queue.Queue()
    for i in range(90):
        t = Downloader(queue)
        t.setDaemon(True)
        t.start()
    for url in urls:
        queue.put(url)
    queue.join()


if __name__ == "__main__":
    
    #####################
    ### INPUTS GO HERE ##
    #####################
    findtag = False
    tag = "richmondmagazine"    
    profile = "renewrichmond"
    number_of_posts_to_scrape = 20
    
    if findtag == True:
        profile = "explore/tags/"+tag

##    number_of_posts_to_scrape = False

    ######################
    ## INPUTS STOP HERE ##
    ######################
    
    driver = webdriver.Firefox()
    urls = scrape_posts(profile,number_of_posts_to_scrape)
    new_urls = []
    for url in urls:
        if findtag == False:
            url = profile+url
        else:
            url = tag+url
        for i in ')"],':
            url = url.replace(i,"")
        url = url.replace("\\","")
        url = url.replace("'s","")
        if "." in url[-1]:
            url = url[0:len(url)-1]
        if "/" in url[-1]:
            url = url[0:len(url)-1]
        if "!" in url[-1]:
            url = url[0:len(url)-1]
        if "?" in url[-1]:
            url = url[0:len(url)-1]
        if ":" in url[-1]:
            url = url[0:len(url)-1]
        if ";" in url[-1]:
            url = url[0:len(url)-1]
        if ".com" not in url:
            new_urls.append(url)
        if ".com" not in url.split("www.instagram.com/")[1]:
            new_urls.append(url)
    urls = list(set(new_urls))
    for i in urls:
        print i
    path = "data/"+profile+".txt"
    filechecker = os.path.isfile(path)
    if filechecker == False:
        main(urls)
    else:
        print "Profile already scraped, please delete the file and re run the scrape"

            
