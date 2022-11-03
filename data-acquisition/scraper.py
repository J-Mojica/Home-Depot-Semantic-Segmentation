import urllib
from googleapiclient.discovery import build


def get_image_urls(resource, query, cx, max_results=100):
    '''
    Returns a list of image urls for a given query
    Service: Google Custom Search API service
    Query: String to search for
    CX: Custom Search Engine ID
    Max_results: Maximum number of results to return
    '''
    # TODO: I think num = max_results is not working. Figure out a way to get more than 10 results
    result = resource.cse().list(q=query, cx=cx, searchType='image', num=max_results).execute()
    return [item['link'] for item in result['items']]

def download_images(urls, category, path="../data"):
    '''
    Downloads images from a list of urls
    Saves to path/category-<filename>
    '''
    for url in urls:
        filename = url.split("/")[-1]
        urllib.request.urlretrieve(url, "{}/{}-{}".format(path, category, filename))

def main():
    ROOM = "kitchen"
    DATA_PATH = "../data/data-raw"
    CX="01259b5c58e404b46"
    API_KEY = open("../api_keys/google_cse.key").read()

    resource = build("customsearch", "v1", developerKey=API_KEY)
    categories = open("../item_categories.txt").read().splitlines()

    for category in categories:
        query = ROOM + " " + category
        print("Querying for {}".format(query))
        urls = get_image_urls(resource, query, CX, max_results=100)
        download_images(urls, category, path=DATA_PATH)

if(__name__ == "__main__"):
    main()