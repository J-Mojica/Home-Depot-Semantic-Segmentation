import os

def check_missing_data(data_path):
    '''
    Checks if there are any missing images in the data folder
    '''
    # Get list of categories
    categories = os.listdir(data_path)
    # Get list of files in each category
    for category in categories:
        files = os.listdir(data_path+"/"+category)
        # Check if there are any files missing
        if(len(files) < 100):
            print(f"\nMissing images for {category}")
            print(f"Found {len(files)} images\n")
        with open(data_path+"/"+category+"/urls.txt") as f:
            urls = f.read().splitlines()
            for i in range(len(urls)):
                url = urls[i]
                filename = url.split("/")[-1]
                if(filename == ""):
                    filename = url.split("/")[-2]
                if("?" in filename):
                    filename = filename.split("?")[0]
                if(filename not in files):
                    print(f"Missing image: {i}\n{filename}\n{url}")


def main():
    data_path = "../data/data-raw"
    check_missing_data(data_path)

if(__name__ == "__main__"):
    main()