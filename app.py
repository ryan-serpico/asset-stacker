from PIL import Image
from statistics import mode
import os

img_folder = os.listdir('img')
img_name_list = []

def getFileNames(dirName):
    '''Collects the file paths in the img folder, appends the img_name_list and sorts them alphabetically'''
    global img_name_list
    for file in dirName:
        img_name_list.append('img/' + file)
    img_name_list.sort()
    return img_name_list

def getImgWidth(img_list):
	'''Goes through each image to find the most common width.'''
	img_width_list = []
	for i in img_list:
		# Get rid of .DS_Store appearing as one of our assets.
		if i == 'img/.DS_Store':
			continue
		else:
			im = Image.open(i)
			img_width_list.append(im.size[0])
	mostCommonWidth = mode(img_width_list)
	return mostCommonWidth

def getImgHeight(img_list, width):
	'''Goes though each image to find the total height of all the assets and header'''
	for i in img_list:
		# We need to resize the header, which tends to be a lot wider than the other assets.
		if i == 'img/0.png':
			baseWidth = width
			img = Image.open('img/0.png')
			wPercent = (baseWidth/float(img.size[0]))
			hSize = int((float(img.size[1])*float(wPercent)))
			img = img.resize((baseWidth, hSize), Image.ANTIALIAS)
			img.save('img/0.png')
		else:
			pass
	img_height = 0
	for i in img_list:
		if i == 'img/.DS_Store':
			continue
		else:
			im = Image.open(i)
			img_height = img_height + im.size[1]
	return img_height

def buildGraphic(width, height, img_list):
	'''Build canvas using width and height data from previous functions, and paste the new images in.'''
	graphic = Image.new('RGB', (width, height))
	y_translate = 0
	for i in img_list:
		if i == 'img/.DS_Store':
			continue
		else:
			im = Image.open(i)
			graphic.paste(im, (0, y_translate))
			y_translate = y_translate + im.size[1]

	graphic.save('img/graphic.png')
	graphic.show()

img_name_list = getFileNames(img_folder)

totalWidth = getImgWidth(img_name_list)

totalHeight = getImgHeight(img_name_list, totalWidth)

buildGraphic(totalWidth, totalHeight, img_name_list)


