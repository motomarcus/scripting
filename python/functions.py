

# As this is interpreted - need to put function defs before
#   code which uses them, so scroll down for the order of execution!

# the basics of function calling
def fibonacci(n):
	"""Print a Fibonacci Sequence up to the value of n"""
	result = []
	a,b = 0,1
	while a < n:
		result.append(a)
		a,b = b, a+b
	return result
	
def paramArrayDemo(*args):
    print "Here's the param array passed in:"
    for arg in args:
        print "Argument: ", arg

# * = arg array, ** = arg dictionary of keyword/value associations
def bikeshop(kind, *arguments, **keywords):
    print "This is bikeshop, called with... ",kind
    
    print "Here's my arg array: "
    for arg in arguments:
        print  arg
        
    print "Here's my dictionary of keywords: "
    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw]

def printRowOfStars():
	print "\n", "    *" * 4


print "\n\n"
x = int(raw_input("Please enter an Integer: "))

print "Here's your fibonacci sequence: ", fibonacci(x)

printRowOfStars()  # yes, you do need the brackets if no args

paramArrayDemo(4,5,6,"seven", "eight")

printRowOfStars()	

bikeshop("Trek", 
		 "Stuff A", "Stuff B",
         index1='First Value', key2="Second Value", ref3="Last Value")
           

           
    