

class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
        self.tricks = []    # creates a new empty list for each dog
        
    def add_trick(self, trick):
        self.tricks.append(trick)


dog1 = Dog('Fido')
dog2 = Dog('Lola')

dog1.add_trick('Roll over')
dog2.add_trick('Play dead')

print dog1.kind
print dog2.kind

print dog1.name, " ", dog1.tricks
print dog2.name, " ", dog2.tricks


print "\nNow for the Shape class..." 

class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    description = "This shape has not been described yet"
    author = "Nobody has claimed to make this shape yet"
    def area(self):
        return self.x * self.y
    def perimeter(self):
        return 2 * self.x + 2 * self.y
    def describe(self,text):
        self.description = text
    def authorName(self,text):
        self.author = text
    def scaleSize(self,scale):
        self.x = self.x * scale
        self.y = self.y * scale
        
# simple inheritance example       
class Square(Shape):
    def __init__(self,x):
        self.x = x
        self.y = x   
    description = "This square has not been described yet"

rectangle = Shape(100,50)
rectangle.describe("A two by one rectangle")
print rectangle.description
print "Perimeter: ", rectangle.perimeter()
print "Area: ", rectangle.perimeter()

sq1 = Square(60)
print sq1.description
print "Sqrs Perimeter: ", sq1.perimeter()
print "Sqrs Area: ", sq1.perimeter()

    