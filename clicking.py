import numpy as np
import pyscreenshot as ImageGrab
import time
import math
from PIL import Image
import pyautogui
import keyboard
from chatgpt import ChatGpt
# Delay to allow switching to the desired screen/window
# time.sleep(3)

# Capture screenshot
# screenshot = ImageGrab.grab()


# takes in a pixel and the visited pixels, checks all around it, return the clump.
def find_neighbors(pixel, allbluepixels, visited=set()):
    neighbors = set([pixel])
    clump = set()
    while len(neighbors)!=0:
        
        currentpixel = neighbors.pop()

        if currentpixel in visited:
            continue
        visited.add(currentpixel)
        clump.add(currentpixel)
        #checking all possible neighbors
        
        possibleneighbors = [(currentpixel[0] + 1, currentpixel[1]), (currentpixel[0] - 1, currentpixel[1]), 
                (currentpixel[0], currentpixel[1] + 1), (currentpixel[0], currentpixel[1] - 1),
                (currentpixel[0] + 1, currentpixel[1] + 1), (currentpixel[0] - 1, currentpixel[1] - 1),
                (currentpixel[0] + 1, currentpixel[1] - 1), (currentpixel[0] - 1, currentpixel[1] + 1)]
        for possibleneighbor in possibleneighbors:
            if possibleneighbor in allbluepixels and possibleneighbor not in visited:
                neighbors.add(possibleneighbor)
                
                
    return clump

#this function works for any function, not just blue.
def BFS(bluepixels, visited):
    largest_clump = []
    for pixel in bluepixels:
        if pixel not in visited:
            current_clump = find_neighbors(pixel, bluepixels, visited)
            if(len(largest_clump) < len(current_clump)):
                largest_clump = current_clump
    return largest_clump
        

def load_image( img ) :
    img.load()
    x,y = img.size
    img = img.resize((int(x/10), int(y/10)), resample=Image.Resampling.BILINEAR)
    data = np.asarray( img, dtype="int32" )
    return data

def save_image( npdata, outfilename ) :
    img = Image.fromarray( np.asarray( np.clip(npdata,0,255), dtype="uint8"), "L" )
    img.save( outfilename )
# Function to check if two RGB values are close
def are_pixels_close(rgb1, rgb2, threshold=30):
    distance = math.sqrt(sum((rgb1[i] - rgb2[i]) ** 2 for i in range(3)))
    return distance <= threshold


def findsumof(lst, n):
    return sum(i[n] for i in lst)
def findcenter(lst):
    xvalue = int(findsumof(lst, 0)/len(lst))
    yvalue = int(findsumof(lst, 1)/len(lst))
    return xvalue, yvalue

while(1):
    
    if keyboard.is_pressed('f'):
        screenshot = ImageGrab.grab()
        # Convert screenshot to numpy array
        img_array = load_image(screenshot)
        1. upload image to url https://stackoverflow.com/questions/29104107/upload-image-using-post-form-data-in-python-requests
        2. run chatgpt "Please respond to this question by color and color only. 
        ex: "Blue", "Red", "Green", "Yellow""
        3. run if statements for color
        # Create a blank array for the result, with the same shape as the screenshot (single channel for grayscale)
        blue_pixel_mask = np.zeros((img_array.shape[0], img_array.shape[1]), dtype=np.uint8)
        allbluepixels = []
        # Define the target blue color
        target_blue = [0, 87, 186]
        4. SET ALL COLORS  
        # Iterate over each pixel to find blue pixels
        for columns in range(img_array.shape[0]):
            for rows in range(img_array.shape[1]):
                if are_pixels_close(list(img_array[columns][rows]), target_blue, threshold=50):
                    # Set the corresponding mask location to white (255) where blue pixels are found
                    blue_pixel_mask[columns][rows] = 255
                    allbluepixels.append((columns, rows))

        clump0 =  (BFS(allbluepixels, set()))
        middlepoint= findcenter(clump0)
        print(middlepoint[0]*10, middlepoint[1]*10)
        pyautogui.click(middlepoint[1]*10, middlepoint[0]*10)
        
        
        
    """fff

print(clump0)
1. upload image
clump0_array = np.zeros((img_array.shape[0], img_array.shape[1]), dtype=np.uint8)
for x,y in clump0:
    clump0_array[x][y] = 100
clump0_array[middlepoint[0]][middlepoint[1]] = 255
# Go over the list and see if any items have the same Y position
# Convert the mask to an image

mask_image = Image.fromarray(clump0_array)
mask_image.show()
"""

"""
ideas for making code faster
- seperate the clumps, then find the largest clump
- allbluepixels to a set
- using a quad-tree or grid system of buckets to find pixels faster 
- tiny monitor - make a smaller screenshot
- decrease number of blue pixels we have
- change possibleneighbors to an offset 
- 
"""

"""
    
    """