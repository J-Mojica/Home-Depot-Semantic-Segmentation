#api_key= AIzaSyBuTl6ZRarT21vdrBeu8gIxLz3alZTb7EM
from image_scraper import get_image_urls, save_urls, download_images
import image_scraper as scraper
from googleapiclient.discovery import build

resource = build("customsearch", "v1", developerKey="AIzaSyBuTl6ZRarT21vdrBeu8gIxLz3alZTb7EM")
query = "kitchen" + " " + "knife"
CX="" #to add Custom Search Engine ID here
urls=scraper.get_image_urls(resource, query, CX, num_results=200)
path="../data"

def test_get_image_urls():
    assert len(urls)>0

def test_save_urls():
    count=0
    save_urls(urls, "knife", path)
    with open(path + "urls.txt", "w") as f:
        for i in range(len(urls)):
            count+=1
    assert count>0

#TODO: find a way to check file size in path/category-<filename>
def test_download_images():
    download_images(urls, "knife", path="../data")
    pass 

