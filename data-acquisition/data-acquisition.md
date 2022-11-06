## Milestone 2

### Image Scapping using Google Custom Search API
#### Steps used:

- Create a Custom Search Engine (CSE) from the Google API console, https://console.cloud.google.com/apis/
  
- Create a [web scraper](image_scraper.py) which uses the Google CSE API to obtain the URLs of images and downloads them

- Created a [driver program](scrape.py) for the [web scraper](image_scraper.py) functions to get the URLs of 200 images
and download them. We acquired double of what's necessary in case some of the URLs do not work or the images are repeated 
instances of others already in the set. Manual clean up will be done at a later stage and the image set will be restricted 
to only 100 images per category. 

- Saved the URLs into a file called "urls.txt" for each category and downloaded the images from those urls. Each
category has its own separate directory and are saved with the name of its respective category followed by a sequential number
for easy identification.

- Downloaded the images using the URLs from these files.