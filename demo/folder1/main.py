import image

def displayImage():
    img = image.Image("/Users/jmadar/Documents/env3d/capu115-assignments/demo/rick-and-morty.jpg")
    width = img.getWidth()
    height = img.getHeight()
    win = image.ImageWin(img.getWidth(), img.getHeight())
    img.draw(win)
    
    
def processFile():
    f = open("data.txt", "r")
    
    sum = 0
    for line in f:
        fields = line.split()
        if fields[0] in 'CD':
            sum = sum + float(fields[4])
    
    f.close()
    return sum

print(processFile())