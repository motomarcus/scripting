#!/usr/bin/perl
use warnings;

# print '\tThis is a single quoted string\n';  #This will treat the \ as literal characters
# print "\tThis is a double quoted string\n";  #This will correctly escape the t and n

print ((3 + 5) / 6, "  ", 8 % 6);

print "\nEnter something interesting\n";
$comment = <STDIN>;


print "fish equals: ",$comment;

print "\n";

$values = 6;
$values += 3;
$values++;
print '$values: ', $values;

print "\n";


