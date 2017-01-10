class tags_dock_data():
    def __init__(self):
        self = self
    def return_tags(self):
        filename = "tags_dock_data.txt"
        with open(filename,'rb') as f:
            data = f.readlines()
        clean_data = []
        hashtags = []
        for i in data:
            line = i.split("\r\n")[0]
            if "    " in line:
                tag = line.split("    ")[1]
                if tag not in hashtags:
                    hashtags.append(tag)
            clean_data.append(line)
        return hashtags

##https://www.google.com/search?q=site:instagram.com/+%2B+%22bill%22&num=100&biw=1745&bih=849&ei=XEnYV6aOBYOi-AH5u7WoDQ&start=100&sa=N
##https://www.google.com/search?q=site:instagram.com/+%2B%22bill%22&num=100&ei=Ii3kV4_LIsTOjwTOnqfQCg&start=100&sa=N&biw=1745&bih=849
##data = tags_dock_data().return_data()
##for i in data:
##    print i
