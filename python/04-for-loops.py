
words = ['cat', 'dog', 'fish', 'duckbilledplatypus']

for w in words:
	print w, len(w)
	
print ""
	
for i in range(len(words)):
	print i, words[i]
	
print ""

# 'else' can be used in for loops...
for n in range(2,20):
	for x in range(2,n):
		if n % x == 0:
			print n, 'equals', x, '*', n/x
			break
	else:
		# ran through the whole for loop without hitting the break...
		print n, 'is a prime number' 
	
	
print ""

for num in range(2,10):
	if num % 2 == 0:
		print 'Found an even number: ',num
		continue #with next iteration of the loop
	print 'Found Non-even number: ',num