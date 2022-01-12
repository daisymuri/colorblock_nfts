# create colorful squares on canvas, 4x4 squares
import random
from color_palettes import *
from PIL import Image, ImageDraw, ImageColor, ImageGrab

# width & height of canvas
w, h =6, 6
#ask user input for width & height
dimensions = eval(input("Please enter desired width & height (ex. [5, 5]) : "))

# func that creates the coordinate points
# i = x width
# j = y height
coordinates = []
left_coordinate = ''
right_coordinate = ''
num_of_boxes = 0
counter = 0

while num_of_boxes < 5:
    # choose random color for canvas
    background_color = random.choice(background_colors)
    # set new canvas
    background = Image.new('RGB', (w, h), background_color)
    #create object used to draw
    pen = ImageDraw.Draw(background, 'RGB')
    # choose random color for squares
    color_palette = random.choice(color_palettes)

    for i in range(1, dimensions[0] + 1):
        for j in range(1, dimensions[1] + 2):
            coordinate = ("(" + str(i) + ", " + str(j) + ")")
            coordinates.append(coordinate)
            # print(coordinate)
            if counter % 2 == 0:
                left_coordinate = coordinate
                # print("left coordinate: " + left_coordinate)
                if right_coordinate in coordinates:
                    # print("next coordinate : " + right_coordinate + left_coordinate)
                    pen.arc([eval(right_coordinate), eval(left_coordinate)], 180, 270, random.choice(color_palette))
            else:
                right_coordinate = coordinate
                # print("complete coordinate: " + left_coordinate + right_coordinate)
                pen.arc([eval(left_coordinate), eval(right_coordinate)], 180, 270, random.choice(color_palette))

            counter+=1
    # image = background.crop((0, 0, 5, 5))
    # image.show()
    background.show()
    num_of_boxes+=1

# matrix 
# 00 10 20 30 40 
# 01 11 21 31 41 
# 02 12 22 32 42 
# 03 13 23 33 43 
# 04 14 24 34 44 

# main()
# background.show()