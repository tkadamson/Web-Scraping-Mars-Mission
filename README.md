# hw-10-mars-mission-web-scraping

## Project Instructions

### Step 1 - Scraping

Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* Create a Jupyter Notebook file called `mission_to_mars.ipynb` and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.

#### NASA Mars News

* Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

```python
# Example:
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."
```

#### JPL Mars Space Images - Featured Image

* Visit the url for JPL Featured Space Image [here](https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html).

* Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

* Make sure to find the image url to the full size `.jpg` image.

* Make sure to save a complete url string for this image.

```python
# Example:
featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars2.jpg'
```

#### Mars Facts

* Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Use Pandas to convert the data to a HTML table string.

#### Mars Hemispheres

* Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

* You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.

* Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.

* Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

```python
# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]
```

- - -

### Step 2 - MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

* Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.

  * Store the return value in Mongo as a Python dictionary.

* Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.

* Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Make sure your template will display a page even if the data is empty.

## Solution Explanation

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
