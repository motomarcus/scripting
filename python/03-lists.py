
even_numbers = [2, 4, 6]
even_numbers.append(8)

print "Here are all the even numbers...",even_numbers

print "and here's just the second: ",
print even_numbers[1]

odd_numbers = range(1,9,2)

print "Here are the odd numbers...",odd_numbers

letters = ['B','C','D','E','F']
print "here are the middle letters: ", letters[1:4]
print "Here is the last letter: ",letters[-1]
letters.insert(0,'A')
print "Adding an A to the start: ", letters
print "Remove last: ",letters.pop()
print "Remove first: ",letters.pop(0)
letters.remove('D')
print "Remove any Ds: ",letters
print "Find location of 'E': ",letters.index('E')


	




