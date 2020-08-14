letters = 'abcd'
numbers = [1,2,3,4]

# stepping in slicing
print(letters[::2]) # ac
print(numbers[::2]) # [1, 3]

class Tree: #class is used to make an object
    def __init__(self, treetype, height):
        self.treetype = treetype #self refers to the object
        self.height = height

pinetree1 = Tree("pine", 1000)
print(pinetree1)
print(pinetree1.treetype)#treetype is a field or a proporty of an object
print(pinetree1.height)

# __name__ == "__main__" when run python test_notes.py
# __name__=="test_notes" when run from another file
print('test_notes:', __name__)

#TODO: search diff between tuple and list
#TODO: for loop, while loop, keyword, function, method, field, object, varible(global, local), value, type
#TODO: collections(lsit,set)

yeet= ["?","!","."]

# while 1==1:
#     print ('YEET OR BE YOTE')#infinite while loop
