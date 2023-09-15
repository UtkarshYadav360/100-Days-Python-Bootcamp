import colorgram

# list of colors from the image
rgb_colors = []

# extracting the colors from the image
colors = colorgram.extract("hirst_image.jpg", 30)

# appending each image color to the "rgb_colors" list
for color in colors:
    # These lines will helps in understanding the code above inside the for loop
    # rgb_colors.append(color)
    # print(rgb_colors)
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

# printing the "rgb_colors" list
print(rgb_colors)
