class log_in():
    def __init__(self,user,pswd,driver):
        self.driver = driver
        self.user = user
        self.pswd = pswd
    def run(self):
        import time
        driver = self.driver
        driver.get('https://www.instagram.com/accounts/login')
        time.sleep(5)
        driver.implicitly_wait(10)
        dom = driver.find_element_by_xpath('//*')
        username = dom.find_element_by_name('username')
        password = dom.find_element_by_name('password')
        login_button = dom.find_element_by_xpath('//*[@class="_aj7mu _taytv _ki5uo _o0442"]')
        username.clear()
        password.clear()
        username.send_keys(self.user)
        password.send_keys(self.pswd)
        time.sleep(5)
        login_button.click()
        time.sleep(5)
        return driver
if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Firefox()
    log_in("imagograzm","Baijo77O",driver).run()
