'''
Driver for the image scraper. 
Takes in a room, list of categories, a path to save images, 
a Google Custom Search Engine ID, and Google API Key.
Downloads images for each product category and saves them to the path.
'''

import image_scraper as scraper
import sys
from googleapiclient.discovery import build
def main():
    ROOM = sys.argv[1] # e.g. "kitchen"
    CATEGORIES_PATH = sys.argv[2] # Path to categories file
    DATA_PATH = sys.argv[3] # Get data path from command line (where to save images)
    CX=sys.argv[4] # Get Custom Search Engine ID from command line
    API_KEY = sys.argv[5] # Get API key from command line

    resource = build("customsearch", "v1", developerKey=API_KEY)
    categories = open(CATEGORIES_PATH).read().splitlines()

    for category in categories:
        query = ROOM + " " + category
        print(f"Querying for {query}")
        urls = scraper.get_image_urls(resource, query, CX, num_results=200)

        # just in case the download fails, save the urls to a file
        # download in separate step
        print(f"Saving {len(urls)} urls for {category}")
        scraper.save_urls(urls, category, path=DATA_PATH)
        
    
    for category in categories:
        urls = open(DATA_PATH+category+"/urls/urls.txt").read().splitlines()
        print(f"Downloading {len(urls)} images")
        scraper.download_images(urls, category, path=DATA_PATH)

    print("Done")
if(__name__ == "__main__"):
    main()