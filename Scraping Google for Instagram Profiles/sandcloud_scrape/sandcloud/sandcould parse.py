all_names = []
pagenums = ["1","2","3","4"]
all_urls = []
for num in pagenums:
    page = "sandcloud" + num + ".txt"
    with open(page, "r") as f:
        data = f.read()
    html_doc = str(data)
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
    print url

##import requests
##for url in urls:
##    r = requests.get(url)
##    data = r.text
    
##    soup = BeautifulSoup(data, 'html.parser')
##    for h3tag in soup.find_all("h3"):
##        print h3tag
    



