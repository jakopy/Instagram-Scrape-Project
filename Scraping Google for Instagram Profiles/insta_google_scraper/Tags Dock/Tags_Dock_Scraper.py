import lxml.html
from lxml.cssselect import CSSSelector
import time
import requests
#categories
def AJAXREQUESTER(url):
    r = requests.get(url)
    category_string = r.text
    import ast
    dic = ast.literal_eval(category_string)
    return dic

url = "https://tagsdock.com/api/list/category?id=0"
categorydic = AJAXREQUESTER(url)
categorylist = categorydic["category"]
master_dic = {}
for i in range(len(categorylist)):
    category = categorylist[i]
    
    url = "https://tagsdock.com/api/list/subcategory?id="+str(i)
    subcategories_dic = AJAXREQUESTER(url)
    subcategory_list = subcategories_dic["category"]

    tagdic = {}
    for j in range(len(subcategory_list)):
        subcategory = subcategory_list[j]
        url = "https://tagsdock.com/api/list/tags?id="+str(i)+"&sid="+str(j)
        tags_dic = AJAXREQUESTER(url)
        tags_list = tags_dic["tags"]

        tagdic[subcategory] = tags_list
        
    master_dic[category]=tagdic
    
##print master_dic

for category in master_dic:
    print "======================="
    print category
    for subcategory in master_dic[category]:
        print "  " + subcategory
        tag_list = master_dic[category][subcategory]
        for tag in tag_list:
            print "    " + tag
