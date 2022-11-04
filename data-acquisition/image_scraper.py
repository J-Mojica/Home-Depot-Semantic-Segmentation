import urllib.request
import os

def get_image_urls(resource, query, cx, num_results=100):
    '''
    Returns a list of image urls for a given query
    Resource: Google Custom Search API resource object
    Query: String to search for
    CX: Custom Search Engine ID
    num_results: Number of results to return
    '''
    urls = []
    # We cannot get more than 10 results per query. So we need to make multiple queries.
    # Each query gets 10 results by default, and they are indexed starting at index 1,
    # then 11, 21, etc. So we need to increment by 10.
    for i in range(1, num_results, 10):
        
        # Perform search and get results starting from index i. 
        result = resource.cse().list(q=query, cx=cx, searchType='image', start=i).execute()

        # The search returns a json object with a key 'items' that contains a list of results.
        # Each item has a field with key 'link' that contains the url.
        # Add the urls to the list. Extend method adds all elements of an iterable to the list.
        urls.extend([item['link'] for item in result['items']])
    return urls

def save_urls(urls, category, path="../data"):
    '''
    Saves a list of urls to a file
    '''
    # Create directory for category if it doesn't exist
    if not os.path.exists(path + "/" + category):
        os.makedirs(path + "/" + category)
    path = path + "/" + category + "/"

    # just in case the download fails
    with open(path + "urls.txt", "w") as f:
        for url in urls:
            f.write(url + "\n")


# TODO: This is not working for some reason
# URLS are saved to a file, but the images are not downloaded
# No need to request Google again for the images, just download them from the urls
def download_images(urls, category, path="../data"):
    '''
    Downloads images from a list of urls
    Saves to path/category-<filename>
    '''
    # Create directory for category if it doesn't exist
    if not os.path.exists(path + "/" + category):
        os.makedirs(path + "/" + category)
    path = path + "/" + category + "/"

    for url in urls:
        # Get the filename from the url
        filename = url.split("/")[-1]
        
        # just in case the url ends with a /
        if(filename == ""):
            filename = url.split("/")[-2]
        

        # Save the image to path/category/filename
        try:
            urllib.request.urlretrieve(url, path + filename)
        except:
            print(f"Could not download: {filename}\n{url}")
