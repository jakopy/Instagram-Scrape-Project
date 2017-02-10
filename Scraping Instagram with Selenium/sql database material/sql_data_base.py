#sqlalchem
class database():
    def __init__(self,path):
        self.path = path
    def create(self):
        path = self.path
        import sqlalchemy
        sqlalchemy.__version__

        from sqlalchemy import create_engine
        engine = create_engine(path)

        from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
        metadata = MetaData()
        users = Table('users', metadata,
                Column('profilename', String, primary_key=True),
                Column('profilepic', String),
                Column('followers', String),
                Column('following', String),
                Column('posts', String),
        )
        self.users = users

        followers = Table('followers', metadata,
              Column('follower', Integer, primary_key=True),
              Column('user_id', None, ForeignKey('users.id')),
        )
        self.followers = followers

        posts = Table('posts', metadata,
              Column('post_id', primary_key=True), #user,timestamp
              Column('user_id', None, ForeignKey('users.id')),
              Column('image'),
              Column('likes', String),
              Column('hastags', String),
              Column('@', String),
              Column('posters_comments', String),
              Column('comments',String),
              Column('Commentors',String),
        )

        self.posts = posts
        metadata.create_all(engine)
        self.engine = engine
    def db_add(self,path,usernames,data):
        if usernames == True:
            from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
            from sqlalchemy import create_engine
            engine = create_engine(path)
            metadata = MetaData()
            users = Table('users', metadata,
                Column('profilename', String, primary_key=True),
                Column('profilepic', String),
                Column('followers', String),
                Column('following', String),
                Column('posts', String),
            )
            ins = users.insert()
            for i in data:
                ins.values(profilename=i)
            ins.compile().params
            conn = engine.raw_connection()
            result = conn.execute(ins)
            
path = r"sqlite:///C:\Users\Jacob\Documents\uber project\Website Scraping\Jacob's Instacrawler\userinputcrawlapp\classy input crawler\testy5.db"
base = database(path)
base.create
##usernames = True
##result = ['This_is_not_a_real_profile_000']
##base.db_add(path,usernames,result)

##path = "sqlite:///C:\Users\Jacob\Documents\uber project\Website Scraping\Jacob's Instacrawler\userinputcrawlapp\classy input crawler\cuhlab.db"
##database_create(path).create()
##
##ins = users.insert()

##str(ins)
#ADDING RULES
##from sqlalchemy import Sequence
##Column('name', String(50))
##users = Table('users', metadata,
##   Column('id', Integer, Sequence('user_id_seq'), primary_key=True),
##   Column('name', String(50)),
##   Column('fullname', String(50)),
##   Column('password', String(12))
##
#insert expressions

##ins = users.insert()
##print str(ins)

##ins = users.insert().values(profilename='imagograzm')
##print str(ins)

##ins.compile().params 


#Executing
##conn = engine.connect()

##print conn

##result = conn.execute(ins)
##print result

##ins.bind = engine
##print str(ins)

##print result.inserted_primary_key

#multiple statements
##ins = users.insert()
##conn.execute(ins,id=2,name="wendy",fullname = "Wendy Williams")
##
##conn.execute(addresses.insert(), [
##    {'user_id': 1, 'email_address' : 'jack@yahoo.com'},
##    {'user_id': 1, 'email_address' : 'jack@msn.com'},
##    {'user_id': 2, 'email_address' : 'www@www.org'},
##    {'user_id': 2, 'email_address' : 'wendy@aol.com'},
## ])
