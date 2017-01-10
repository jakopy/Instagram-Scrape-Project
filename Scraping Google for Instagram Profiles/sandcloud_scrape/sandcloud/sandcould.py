import requests
##page = "https://www.google.com/search?q=site:instagram.com+%2B+%22%23sandcloudtowels%22&biw=1536&bih=735&ei=1TZxWNbMEsGImQGf3r6wCQ&start=100&sa=N&bav=on.2,or.r_cp.&bvm=bv.142059868,d.eWE"
##page = "https://www.google.com/search?num=100&biw=1536&bih=735&q=site%3Ainstagram.com+%2B+%23sandcloudtowels&oq=site%3Ainstagram.com+%2B+%23sandcloudtowels&gs_l=serp.3...205934.209745.0.210157.6.5.1.0.0.0.152.501.2j3.5.0....0...1c.1.64.serp..1.0.0.MGLcAuvF_vk"
##page = "https://www.google.com/search?q=site:instagram.com+%2B+%22%23sandcloudtowels%22&num=100&biw=1536&bih=735&ei=BkFxWKLfH8WYmQHxyoDwAw&start=0&sa=N"
##page = "https://www.google.com/search?num=100&biw=1536&bih=735&q=site%3Ainstagram.com+%2B+sandcloudtowels&oq=site%3Ainstagram.com+%2B+sandcloudtowels&gs_l=serp.3...15144.15144.0.15476.1.1.0.0.0.0.64.64.1.1.0....0...1c.1.64.serp..0.0.0.zbYXGeudg14"
##page= "https://www.google.com/search?q=site:instagram.com+%2B+sandcloud+towels&num=100&biw=1536&bih=735&ei=uEJxWKD-IcHemAHKz7KACA&start=100&sa=N"
pagenumbers = ["0","100","200"]
for pages in pagenumbers:
    page = "https://www.google.com/search?q=site:instagram.com+%2B+sandcloud+towels&num=100&biw=1536&bih=735&ei=skNxWJu0A4PJmwG-l7PACA&start="+pages+"&sa=N"
    r = requests.get(page)
    print r.text
