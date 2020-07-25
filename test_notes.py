letters = 'abcd'
numbers = [1,2,3,4]

# stepping in slicing
print(letters[::2]) # ac
print(numbers[::2]) # [1, 3]

class Tree:
    def __init__(self, treetype, height):
        self.treetype = treetype
        self.height = height

pinetree1 = Tree("pine", 1000)
print(pinetree1)
print(pinetree1.treetype)
print(pinetree1.height)
