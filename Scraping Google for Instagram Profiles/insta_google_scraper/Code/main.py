from insta_google import instagoogle
from tagsdockreader import tags_dock_data

data = tags_dock_data().return_tags()
tagnumber = 0
with open("instagram_profile_store.txt","w") as f:
    for tag in data:
        print tag
        #NOTE: the search url in instagoogle accounts for a tag by adding %23 in the search url
        #Read googleurl.txt
        tag = tag.replace("#","")

        search = instagoogle(tag)
        insta_profiles = search.run_regular()

        ##instagram_profile_store
        f.write("==================="+"\n")
        f.write(tag +"\n")
        f.write("==================="+"\n")        
        for i in insta_profiles:
            f.write(i+"\n")
    f.close()


