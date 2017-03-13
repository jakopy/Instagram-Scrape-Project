======
 Installation
========

1. If you already have firefox please uninstall it from your computer
2. Install Firefox version 33 here: https://ftp.mozilla.org/pub/firefox/releases/33.0/win32/en-US/
3. install selenium version 2.53 by going to command line and typing in pip install selenium==2.53 and pip install requests
4. Run any python program to see what it does, enjoy :)

========
Module Requirements
========
python2 </br>
pip install selenium==2.53 </br>
pip install requests </br>

======
How Scrape Different Profiles
=======


<h3> The code </h3> 
209    ##################### </br>
210    ### INPUTS GO HERE ## </br>
211    ##################### </br>
212    findtag = False       </br>
213    tag = "richmondmagazine"   </br> 
214    profile = "renewrichmond"</br>
215    number_of_posts_to_scrape = 20</br>

<ul>
      <li>Note on line 212: if you change this line in the code to findtag = True the tag = "richmondmagazine" will be the tag that will be scraped </li>
      <li>Note on line 213: this is the name of a tag that you will want to scrape, if you use a # then the scrape will be unsuccessful, please do not add this to the search, only the literal name of the tag can be scraped example: "#sunglasses" will not scrape #sunglasses but "sunglasses" will scrape "#sunglasses"</li>
      <li>Note on line 214: this is the name of a profile that you will want to scrape, make sure that findtag = False in order to scrape a profile. profile = "nectar", findtag = "False" will scrape nectar's posts. </li>
      <li>Note on line 215: If you set the number_of_posts_to_scrape = False, this will tell the scraper to scrape all of a persons posts based on the number of posts that a user has. Otherwise you may enter the number of posts you wish to scrape from a profile, example: number_of_posts_to_scrape = 50. </li>      
</ul>


