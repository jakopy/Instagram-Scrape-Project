#create a new database for a new day

class database_create():
    def __init__(self):
        self = self
    def create(self):                
        from datetime import *
        todays_date = str(datetime.now())
        todays_date = todays_date.split(",")[0]
        todays_date = todays_date.split(" ")[0]
        year = todays_date.split("-")[0]
        month = todays_date.split("-")[1]
        day = todays_date.split("-")[2]
        todays_date = month + "-" + day + "-" + year
        new_db_path = "data/"+todays_date+".db"
        try:
            import sqlite3
            conn = sqlite3.connect(new_db_path)
            c = conn.cursor()
            c.execute('''CREATE TABLE users
                         (user_id, password, profile_description, followers, following, posts)''')
            c.execute('''CREATE TABLE followers
                         (follower, user_id)''')
            c.execute('''CREATE TABLE posts
                         (post_id, user_id, image, likes, hashtags, at symbol, posters_comments, comments, Commentors)''')
            conn.commit()
            conn.close()
        except Exception as e:
            "do nothing"
        return new_db_path



