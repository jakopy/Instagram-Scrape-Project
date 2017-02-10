############
### MAIN ###
############
##import argparse
##import codecs
##import logging
####import os
##import pdb
##import re
##import time
##import traceback
##from urlparse import urljoin
##import warnings

from requests_futures.sessions import FuturesSession
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
driver = webdriver.Firefox(capabilities=firefox_capabilities)
##import shutil

##shutil.rmtree('c:\\users\\jacobi~1\\appdata\\local\\temp\\tmpepdmhm.webdriver.xpi\\platform\\WINNT_x86-msvc\\components')


##driver = webdriver.Firefox()

#################################################################################################################################################################################
####################################################################################################################################################################################
############ JOB 1 ########################################################################################################################################################################
####################################################################################################################################################################################
####################################################################################################################################################################################

from database_creator import database_create
newdb = database_create()
new_db_path = newdb.create()

from log_bot import log_in
log_in_user = log_in("imagograzm","Baijo77O",driver)
driver = log_in_user.run()

from follow_bot import followcrawl
run1 = followcrawl("instagram",100,True,driver)
result = run1.run()
new_data = result

from sqlite_db_cache import sql_cache
add_to_cache = sql_cache('user_names',new_data,new_db_path)
add_to_cache.adder()

#make dupcheck a rule either yes or no
#make a database for each day run
#put the database writing into its own thread
#once you go multithreaded everything is multithreaded

#GATHER ALL DATA FIRST THEN ADD IT TO THE DATABASE
#Batching is groupings

#if I can eliminate selenium then do it

from sqlite_db_cache import data_base_getter
current_database = data_base_getter('followers',new_db_path)
data = current_database.get()

new_profiles_to_scrape = []
for user in data:
    followers = data[user]
    if followers == None:
        new_profiles_to_scrape.append(user)
        
from profile_bot import profile_bot
profiletorun = profile_bot(new_profiles_to_scrape,driver)
data = profiletorun.run()

from sqlite_db_cache import sql_cache
add_to_cache = sql_cache('add_profile_info',data,new_db_path)
add_to_cache.adder()

#################################################################################################################################################################################
####################################################################################################################################################################################
############ JOB 2 PT 1 ########################################################################################################################################################################
####################################################################################################################################################################################
####################################################################################################################################################################################

#post crawler
