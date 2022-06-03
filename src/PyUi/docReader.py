import os


mylist = []

def DocRead():
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            splitFile= name.split(".")
            if splitFile[len(splitFile)-1]=="jpg" or splitFile[len(splitFile)-1]=="jpg":
                mylist.append(os.path.join(root, name))
            
    #for name in dirs:
    #    print(os.path.join(root, name))
    
print("a")