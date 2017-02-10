class followcrawl():
    def __init__(self,profile,numfollowers,allfollowers,driver):
        self.profile = profile
        self.numfollowers = numfollowers
        self.allfollowers = allfollowers
        self.driver = driver
    def run(self):
        import time
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        from selenium.common.exceptions import NoSuchElementException, TimeoutException


        driver = self.driver
        url = "https://instagram.com/" + self.profile
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
        driver.execute_script("window.scrollTo(0, 10000);")
                
        selfnumber = self.numfollowers
        if self.allfollowers == True:
            selfnumber = allfollowernumber
        if allfollowernumber > self.numfollowers:
            selfnumber = self.numfollowers
        if selfnumber > cur_follow_num:
            element = List.find_elements_by_xpath('*')[-1]
##        while True:
##            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
##            time.sleep(3)
        print len(List.find_elements_by_xpath('*'))
        print selfnumber
        while len(List.find_elements_by_xpath('*')) < selfnumber:
            element.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)

        cur_follow_num = len(List.find_elements_by_xpath('*'))
        for _ in range(2*(selfnumber - cur_follow_num)/10):
            element.send_keys(Keys.PAGE_DOWN)
##
        followers =  []
        for ele in List.find_elements_by_xpath('*')[:selfnumber]:
            followers.append(ele.text.split('\n')[0])
            
        return followers
#main

