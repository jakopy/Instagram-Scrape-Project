################################
#  CREATING DATA BASE
###########################

##import sqlalchemy
##sqlalchemy.__version__
##
##from sqlalchemy import create_engine
##
##path = r"sqlite:///C:\Users\Jacob\Documents\uber project\Website Scraping\Jacob's Instacrawler\userinputcrawlapp\classy input crawler\sql database material\foo2.db"
##engine = create_engine(path)
##
##from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
##metadata = MetaData()
##users = Table('users', metadata,
##     Column('id', Integer, primary_key=True),
##     Column('name', String),
##     Column('fullname', String),
##)
##
##addresses = Table('addresses', metadata,
##   Column('id', Integer, primary_key=True),
##   Column('user_id', None, ForeignKey('users.id')),
##   Column('email_address', String, nullable=False)
##)
##
##metadata.create_all(engine)



###################################
# INSERT COMMANDS
###########################################

##ins = users.insert()
##ins = users.insert().values(name='jack', fullname='Jack Jones')
##ins.compile().params
##conn = engine.connect()
##result = conn.execute(ins)

##ins.bind = engine
##result.inserted_primary_key


#######################################
# EXECUTING SQL COMMANDS
##########################################

from sqlalchemy import create_engine
from sqlalchemy import *
path = "C:\Users\Jacob\Documents\uber project\Website Scraping\Jacob's Instacrawler\userinputcrawlapp\classy input crawler\cuhlab.db"
engine = create_engine(r"sqlite:///"+path)
connection = engine.connect()


##conn = engine.connect()
##trans = conn.begin()
#engine won't do anything unless it's actually connected
result = engine.execute("select * from users")
##result.delete()
##from sqlalchemy.sql import table, column, select
##t = table('users')
import sqlalchemy
sqlalchemy.sql.expression.delete(table, whereclause="select * from users where id=2", bind=None, returning=None, prefixes=None)
##engine.execute("Delete from users where user_id = 2")
all_users = result.fetchall()
##all_users.query.filter_by(id=2).delete()
for row in all_users:
    print row
##trans.commit()
##conn.close()
#row["emp_name"]
#row.emp_id
#row["emp_id"]
#result.close() #closes the row entirely
#for row in result:
#   print row
#row.keys()
#dict(row)


#inserting values in to an existing table
##engine.execute("insert into employee (emp_name) values (:name)", name = 'dilbert')

#fetching all items from database
##result = engine.execute("select * from employee")
##result.fetchall()
#row.keys()
#dict(row)


#transaction
#conn = engine.connect()
#trans = conn.begin()
#conn.execute("insert into employee (emp_name) values (:emp_name)", emp_name = "wendy")
#conn.execute("update employee_of_month set emp_name =:emp_name",emp_name = "wendy")
#trans.commit()
#conn.close()

#engine.execute("insert into employee (emp_name) values('dilbert')")
