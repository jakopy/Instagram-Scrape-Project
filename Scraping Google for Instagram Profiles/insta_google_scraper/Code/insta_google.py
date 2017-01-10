class instagoogle():
    def __init__(self,searchterm):
        self.searchterm = searchterm

    def run_regular(self):
        import lxml.html
        from lxml.cssselect import CSSSelector

        # get some html
        import requests
        profiles = []
        searchterm = self.searchterm

        #get page numbers        
        morepages = ["0"]
        for i in range(1,10,1):
            newpage = str(i)+"00"
            morepages.append(newpage)
            
        result_checker = 1
        import time
##        for i in morepages:
##            if result_checker > 0:
                    #a sleeper in case of too many requests
    ##                time.sleep(10)
##        pagenum = i
    ##                page = "https://www.google.com/search?q=site:instagram.com/+%2B+%23"+searchterm+"&num=100&ei=Yn7kV9j9MYvi-QHC9KsI&start="+pagenum+"&sa=N&biw=1745&bih=849"
##        page="https://www.google.com/search?q=site:instagram.com+%2B+%22%23sandcloudtowels%22&biw=1536&bih=735&ei=1TZxWNbMEsGImQGf3r6wCQ&start=10&sa=N&bav=on.2,or.r_cp.&bvm=bv.142059868,d.eWE"
        page = "https://www.google.com/search?q=site:instagram.com+%2B+%22%23sandcloudtowels%22&biw=1536&bih=735&ei=1TZxWNbMEsGImQGf3r6wCQ&start=10&sa=N&bav=on.2,or.r_cp.&bvm=bv.142059868,d.eWE"
        headers = {
           'User-agent': 'Mozilla/5.0',
            }
        
        r = requests.get(page , headers=headers)
        print r.text
        # build the DOM Tree
        tree = lxml.html.fromstring(r.text)
        # print the parsed DOM Tree
        # print lxml.html.tostring(tree)

        # construct a CSS Selector
        sel = CSSSelector('h3')
        
        # Apply the selector to the DOM tree.
        results = sel(tree)
##                print results
        result_checker = len(results)
        for result in results:
            entiretag = lxml.html.tostring(result)
##                    print entiretag
            if 'instagram.com/' in entiretag:
                partial_tag = entiretag.split('instagram.com/')[1]
##                print partial_tag
                profile = partial_tag.split("/")[0]
                if "&amp;" in profile:
                    profile = profile.split("&amp;")[0]
                if profile != "p":
                    if "%" not in profile:
                        profiles.append(profile)
        return profiles

if __name__ == "__main__":
    surf_search = instagoogle("sandcloudtowels")
    surf_profiles = surf_search.run_regular()
##    for i in surf_profiles:
##        print i
