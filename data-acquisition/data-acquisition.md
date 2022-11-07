## Milestone 2

### Image Scapping using Google Custom Search API
#### Steps used:

- Create a new project in [Google API cloud console](https://console.cloud.google.com/apis/dashboard))

- In this new project, enable the Custom Search API.

- Go to the credentials tab on the dashboard and acquire an API key for the Custom Search API

- Go to the [Programmable Search Engine Control Panel](https://programmablesearchengine.google.com/controlpanel/all) and add a new 
custom search engine, making sure to enable image search. Then get the Search Engine's ID in it's overview page after adding it.
  
- Create the functions for a [web scraper](image_scraper.py) which uses the Google API Python Client to access a Custom Search Engine resource
 to obtain the URLs of images and downloads them.

- Created a [driver program](scrape.py) for the [web scraper](image_scraper.py) functions to get the URLs of 200 images
and download them. We acquired double of what's necessary in case some of the URLs do not work or the images are repeated 
instances of others already in the set. Manual clean up will be done at a later stage and the image set will be restricted 
to only 100 images per category. 

- Saved the URLs into a file called "urls.txt" for each category and downloaded the images from those urls. Each
category has its own separate directory and are saved with the name of its respective category followed by a sequential number
for easy identification.
