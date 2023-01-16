import os
import sys
import random


def clean_data(DATA_PATH):
    for category in os.listdir(DATA_PATH):

        path = DATA_PATH + category + "/"

        files = os.listdir(path)

        # Randomized the order of the files
        # So that they aren't in the same order
        # as they were downloaded
        random.shuffle(files)

        # Remove everything that's not a .jpg file just in case
        # leave directories untocuhed
        for file in files:
            file_type = file.split(".")[-1]
            if os.path.isfile(path+file):
                if(file_type != "jpg" and file_type != "jpeg"):
                    os.remove(path+file)

        # Rename all files to be in the format of category_1.jpg, category_2.jpg, etc.
        for i in range(len(files)):
            file = files[i]
            if os.path.isfile(path+file):
                # Max 100 images per category (we start with image 0 -> 99)
                if(i > 99):
                    os.remove(path+file)
                else:
                    os.rename(path+file, f"{path}{category}_{str(i)}.jpg")
def main():
    if(len(sys.argv) != 2):
        print("Usage: python clean_data.py [data_path]")
        return
    DATA_PATH = sys.argv[1]
    clean_data(DATA_PATH)

if __name__ == "__main__":
    main()