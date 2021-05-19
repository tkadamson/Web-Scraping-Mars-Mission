# Web-Scraping-Mars-Mission

### Summary | GRADE: A
For this project, I was tassked with scraping various images and statistics related to NASA's Mars Missions using Python's BeautifulSoup and Splinter modules. Then I built a Flask App API with the scraped data, and used an HTML template to display the collected data. 

### Project Writeup

#### Web Scraping
For the initial Jupyter Notebook web scrape, I divided it into four sections, one for each new website to scrape. 

The first section was the NASA News site. After initializing the splinter browset and scraping the page into a BeautifulSoup object, I used the inspector tool to find which html tag and class contained the relevent infomation. The title was contained within the class 'content_title' and the tag was contained within the class'article_teaser_body'. Using find_all() I placed the text into variables.

The second section contained the current JPL featured Mars image. Simlar to above, I found the class 'headerimage' which contained the path to the image, and used find() to place it in a variable.

Next was scraping a table of Mars facts using Pandas and converting it to html. Using read_html(), I found all the tables on the page, and found the desired table at index 0. I renamed the columns, reset the index, and stored the html code using to_html().

Lastly was getting the four hemisphere images astrogeology.usgs.gov. After initializing the browser, I scraped the name of each hemisphere and put the names into a list so I could use the names to navigate the splinter browser. I then ran those names through a loop, which initiated a new Browser session and used splinter to click the link with the listed hemisphere name. Once I got to the new page, I was able to find the proper tag and class to get the image path. Then I stored both the hemisphere name and link in a dictionary. 

Once the initial scrape was completed, I used the code within a Python script, under a function scrape_info. Then I took each of the scrape elements andd placed them into a single dictionary to be returned. 

#### Flask App
After Flask initialization, I created two routes: one as a landing and one to call the python scrape script. The second route used the scrape_info function to grab the data, and then store it in a Mongo Database. It then redirects you back to the home page. 

The home page takes the Mongo Dictionary, and passes it into a render template. 

The render template, index.html creates the page which contains a button that runs the scrape route from the flask app. Using the Bootstap grid, I created a template to display each scraped element. At the top, the JPL image, then a second section with the latest news and the table facts side by side. Lastly, a row containing the titles and images for each hemisphere. 
