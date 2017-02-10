#chachey
#NOTES:

#database.txt
#1line database.txt exmple
#profilename,last_updated,pswd,[follower1,follower2],[following1,following2],{post_id:[like_count,video?,hashtags,posters_comments]}


#profilename,last_updated,pswd,followers_bank,following_bank,post_bank

#followers_bank = [follower1,follower2]
#following_bank = [following1,following2]
#post_bank = {post_id:[like_count,video?,hashtags,posters_comments]}





##pswd = current_data.split(",")[1]
##followers = current_data.split(",")[2]
##following = current_data.split(",")[3]
##posts_bank = current_data.split(",")[4]
##posts_bank_count = len(posts_bank)



def post_data_adder(post_data,current_profile):
    grab_current_cache
    
    with open("data/" + "database.txt") as f:
        current_data = f.readlines()
        for profiledata in current_data:
            profilename = current_data.split(",")[0]
            if current_profile in current_data:
                posts_bank = current_data.split(",")[4]
                posts_bank_count = len(posts_bank)
    
    for post_ids in posts_bank:
        db_time_stamps = post_ids.split("_")[1]

    #check to see if post in database
        
    if post_time_stamp not in db_time_stamps:
        #add new post instance
        post_number = posts_bank_count + 1
        post_id = post_number + "_" + post_time_stamp
        
    #current posts in bank
    comment_list_in_cache = []
    for post_id in post_data:
        info = post_data[post_id]
        comment_list_in_cache.append(info[2])
    if posters_comment not in comment_list_in_cache:
        newpost_id = uuid.uuid4()
