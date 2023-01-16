import os
import random
import image_scraper as scraper

category = "toaster"
files = os.listdir(f'./data/data-raw/{category}')

nums = [ str(i) for i in range(100)]
for i in range(len(files)):
    file = files[i]
    if file.endswith('.jpg'):
        num = file.split(".")[0].split("_")[1]
        if num in nums:
            nums.remove(num)
print(len(files))
print("Missing: ", nums)

i = 0
curr = nums[i]
urls = open(f'./data/data-raw/{category}/urls/urls.txt', 'r').readlines()
while(len(files) < 101):
    url = urls[random.randint(0, len(urls)-1)]
    
    filename = url.split("/")[-1]

    # just in case the path ends with a /
    if filename == "":
        filename = url.split("/")[-2]

    # if the filename has a query string, remove it
    if "?" in filename:
        filename = filename.split("?")[0]

    # get the image type
    image_type = filename.split(".")[-1]

    # if the image type is not jpg skip it
    if image_type not in ["jpg", "jpeg"]:
        continue
    scraper.download_image(url, f'./data/data-raw/{category}/', f'{category}_{curr}.jpg')
    i += 1
    curr = nums[i%len(nums)]
    files = os.listdir(f'./data/data-raw/{category}')
