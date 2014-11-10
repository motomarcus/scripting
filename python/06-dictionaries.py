tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127  # add new item
print "Phone list: ",tel

print "Jack's number: ", tel['jack']

tel['sape'] = 9987
print "Modified Sape's number ",tel

print "Just the keys: ", tel.keys()

print "Is guido in the dict? ", 'guido' in tel