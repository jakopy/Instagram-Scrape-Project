class searcher():
    def __init__(self,search_string,search_type,follow_range):
        self.search_string = search_string
        self.search_type = search_type
        self.follow_range = follow_range
    def get_db_results(self):
        if self.search_type =="users":
            import sqlite3
            database_name = "data/master.db"
            conn = sqlite3.connect(database_name)
            c = conn.cursor()
            user = self.search_string
            execute_string = "SELECT " + "*" + " FROM users"
            user_data = c.execute(execute_string)
            all_user_names = []
            min_followers = int(self.follow_range[0])
            max_followers = int(self.follow_range[1])
            for i in user_data:
                if user in i[0]:
                    followers = i[4]
                    if min_followers <= followers <= max_followers:
                        userdata = i
                        link = "http://www.instagram.com/"+i[0]
                        new = userdata+(link,)
                        all_user_names.append(new)
        return all_user_names
    
if __name__ == "__main__":
    search = searcher("juan","users").get_db_results()
