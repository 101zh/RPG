import random
from tkinter import Button
import pandas as pd
import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((1600, 1000)) 
pygame.display.set_caption("Testing")
x=50
y=50
width=40
height=60
vel=5

fight_btn=pygame.image.load("fightbtn.png").convert_alpha()

class btn():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def exist(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action

fight_btn= btn(200, 200, fight_btn, 10)


run = True
while run:

	screen.fill((202, 228, 241))

	if fight_btn.exist(screen):
		print('Fought')

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()

# letters = 'abcd'
# numbers = [1,2,3,4]

# # stepping in slicing
# print(letters[::2]) # ac
# print(numbers[::2]) # [1, 3]

# class Tree: #class is used to make an object
#     def __init__(self, treetype:str, height:int):
#         self.treetype = treetype #self refers to the object
#         self.height = height

# pinetree1 = Tree("pine", 1000)
# print(pinetree1)
# print("this is the type"+pinetree1.treetype)#treetype is a field or a proporty of an object
# print("this is the height"+str(pinetree1.height))
# pinetree1.height+=5
# print("the tree grew by 5 it is now "+str(pinetree1.height))
# __name__ == "__main__" when run python test_notes.py
# __name__=="test_notes" when run from another file
# print('test_notes:', __name__)

#TODO: search diff between tuple and list
#TODO: for loop, while loop, keyword, function, method, field, object, varible(global, local), value, type
#TODO: collections(lsit,set)

# yeet= ["?","!","."]

# while 1==1:
#     print ('YEET OR BE YOTE')#infinite while loop

dictionary = {
    "type":"water",
    "hp":"50"
}

# print(dictionary)

# list1=[1,2,3,4,5,6,7,8,9,0]

# print (list1[5])

# for i in list1:
#     print ("for number of things in list1 print that amount")

#print = [0,1,2,3] this is an example of a keyword print
# f=5
# f=range(f)
# for i in f:
#     print("lol")
# myfile = open("test.txt", "rt") # open test.txt for reading text
# contents = myfile.read()         # read the entire file to string
# myfile.close()                   # close the file
# print(contents)                  # print string contents

# data=pd.read_csv("test.csv")# reading the csv file
# data.loc[0, "level"]="AAAAAAAAAAAAAAAAAAAA"# updating the column value/data
# data.to_csv("test.csv", index=False) # writing into the file
# print(data)
