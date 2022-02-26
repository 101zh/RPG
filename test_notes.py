import random
import pandas as pd
# letters = 'abcd'
# numbers = [1,2,3,4]

# # stepping in slicing
# print(letters[::2]) # ac
# print(numbers[::2]) # [1, 3]

class Tree: #class is used to make an object
    def __init__(self, treetype:str, height:int):
        self.treetype = treetype #self refers to the object
        self.height = height

pinetree1 = Tree("pine", 1000)
print(pinetree1)
print("this is the type"+pinetree1.treetype)#treetype is a field or a proporty of an object
print("this is the height"+str(pinetree1.height))
pinetree1.height+=5
print("the tree grew by 5 it is now "+str(pinetree1.height))
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

print(dictionary)

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
