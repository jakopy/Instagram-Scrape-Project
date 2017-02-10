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
