import os

files = os.listdir('./')

nums = [ str(i) for i in range(100)]
for i in range(len(files)):
    file = files[i]
    if file.endswith('.jpg'):
        num = file.split(".")[0].split("_")[1]
        if num in nums:
            nums.remove(num)
print("Missing: ", nums)
