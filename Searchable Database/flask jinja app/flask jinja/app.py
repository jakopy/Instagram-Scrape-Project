from flask import Flask, render_template, request
app = Flask(__name__)
##@app.route('/not_hello')
##def index():
##    lst = ['blah',12,65,84,75,67,77,'love me']
##    return render_template("not_hello.html", nums=lst)

@app.route('/instagram_search',methods=['GET','POST'])
def send():
    if request.method == "POST":
        search_term = request.form['search_term']
        max_followers = request.form['Max_Follower_Filter']
        min_followers = request.form['Min_Follower_Filter']
        follow_range = [min_followers,max_followers]
        from searcher import searcher
        data = searcher(search_term,"users",follow_range).get_db_results()
        return render_template('search_results.html',search_term=search_term,data=data)
    return render_template('instagram_search.html')
if __name__ == "__main__":
    app.run()
    
