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
    filel=file.lower()
    if filel.endswith(".jpeg") or filel.endswith(".png") or filel.endswith(".gif"):
        path_file = os.path.abspath(file)
        os.rename("/Users/krzysztof/Downloads/%s" %file, "/Users/krzysztof/Downloads/images/%s" %file)
    elif filel.endswith(".xlsx") or filel.endswith(".docx") or filel.endswith(".pdf"):
        path_file2 = os.path.abspath(file)
        os.rename("/Users/krzysztof/Downloads/%s" %file, "/Users/krzysztof/Downloads/documents/%s" %file)
    


