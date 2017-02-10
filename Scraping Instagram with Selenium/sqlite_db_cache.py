class sql_cache():
    def __init__(self,scrape_type,new_data,database_name):
        import sqlite3
        self.scrape_type = scrape_type
        self.new_data = new_data
        self.database_name = database_name
    def adder(self):
        def checker(scrape_type,new_data,database_name):
            import sqlite3
            if scrape_type == "user_names":
                conn = sqlite3.connect(database_name)
                c = conn.cursor()
                current_data = c.execute("SELECT user_id from users")
                currdata = []
                for row in current_data:
                    currdata.append(row[0])
                not_in_db = []
                for profilename in new_data:
                    if profilename not in currdata:
                        not_in_db.append(profilename)
                conn.close()
                return not_in_db
            if scrape_type == "add_profile_info":
##                conn = sqlite3.connect(database_name)
##                c = conn.cursor()
##                current_data = c.execute("SELECT * from users")
##                currdata = []
##                for row in current_data:
##                    user_id = row[0]
##                    pswrd = row[1]
##                    prof_description= row[2]
##                    followers = row[3]
##                    following = row[4]
##                    posts = row[5]
##                    currdata.append(row[0])
##                conn.close()
                #update check if value already exists
                #or just redo value everytime this runs?
                #right now the checker will not do anything with add profile_info

                return new_data
            
        data_to_add = checker(self.scrape_type,self.new_data,self.database_name)
        
        def user_name_formater(data,scrape_type):
            if scrape_type == "user_names":
                new = {}
                for user_id in data:
                    new[user_id] = [None,None,None,None,None]
                return new
            if scrape_type == "add_profile_info":
                return data
        new = user_name_formater(data_to_add,self.scrape_type)
        
        #add it
        if self.scrape_type == "user_names":
            import sqlite3
            conn = sqlite3.connect(self.database_name)
            c = conn.cursor()
            for i in new:
                c.execute("INSERT INTO users VALUES(?,?,?,?,?,?)",(i,new[i][0],new[i][1],new[i][2],new[i][3],new[i][4]))
            conn.commit()
            conn.close()
        if self.scrape_type == "add_profile_info":
            import sqlite3
            conn = sqlite3.connect(self.database_name)
            c = conn.cursor()
            for user in new:
                password = None
                profile = user
                description = new[user][0]
                postnumber = new[user][1]
                follownumber = new[user][2]
                followingnumber = new[user][3]

                
                c.execute('''UPDATE users SET profile_description = ? WHERE user_id = ? ''', (description,profile))
                c.execute('''UPDATE users SET followers = ? WHERE user_id = ? ''', (follownumber,profile))
                c.execute('''UPDATE users SET following = ? WHERE user_id = ? ''', (followingnumber,profile))
                c.execute('''UPDATE users SET posts = ? WHERE user_id = ? ''', (postnumber,profile))
                
            conn.commit()
            conn.close()
##            import sqlite3
##            conn = sqlite3.connect(self.database_name)
##            c = conn.cursor()
##            for i in new:
##                c.execute("INSERT INTO users VALUES(?,?,?,?,?,?)",(i,new[i][0],new[i][1],new[i][2],new[i][3],new[i][4]))
##            conn.commit()
##            conn.close() 
            
import sqlite3

class data_base_getter():
    def __init__(self,get_type,database_name):
        self.get_type = get_type
        self.database_name = database_name
    def get(self):
        get_type = self.get_type
        database_name = self.database_name
        if get_type == "user_names":
            import sqlite3
            conn = sqlite3.connect(self.database_name)
            c = conn.cursor()
            userdata = c.execute("SELECT user_id FROM users")
            data = []
            for row in userdata:
                data.append(row[0])
            return data
        if get_type == "followers":
            import sqlite3
            conn = sqlite3.connect(self.database_name)
            c = conn.cursor()
            userdata = c.execute("SELECT * FROM users")
            data = {}
            for row in userdata:
                data[row[0]]=row[3]
            return data

class data_deleter():
    def __init__(self,delete_type,database_name):
        self.delete_type = delete_type
        self.database_name = database_name
    def delete(self):
        if self.delete_type == "Null followers":
            import sqlite3
            conn = sqlite3.connect(self.database_name)
            c = conn.cursor()
            users_to_delete = c.execute("SELECT * FROM users")
            users = []
            for row in users_to_delete:
                if row[3] == None:
                    users.append(row[0])
            for user in users:
                c.execute("DELETE FROM users WHERE user_id = ?",(user,))
            conn.commit()
            conn.close()
        
#main
    
##new_data = ["imagograzm","instagram"]
##add_to_cache = sql_cache('user_names',new_data,"cuhlab.db")
##add_to_cache.adder()
##current_database = data_base_getter('user_names',"cuhlab.db")
##data = current_database.get()
data = data_deleter("Null followers","data/09-07-2016.db")
data.delete()
