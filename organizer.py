import os

images = "images"
documents = "documents"

parent_dir= "/Users/krzysztof/Downloads"

path1 = os.path.join(parent_dir, images)
path2 = os.path.join(parent_dir, documents)

while True:
    try:
        os.mkdir(path1)
        os.mkdir(path2)
        print("Directory '%s' created" % images)
        print("Directory '%s' created" % documents)
        break
    except FileExistsError:
        print("Files in Downloawds Directory")
        break
 
pliczki = os.listdir(parent_dir)

for file in pliczki:
    if flie.endswith(".jpg") or flie.endswith(".png") or flie.endswith(".gif"):

    elif flie.endswith(".jpg") or flie.endswith(".png") or flie.endswith(".gif"):


print(pliczki)
