#!/usr/bin/perl
use warnings;
use strict;

my $test = 30;

print ("one", " ", "two", " ", "three");
print "\n";
print (123,456,789,$test,"\n");
print ("Can I put a numeric variable in a string thus:$test?\n");
print ('Yes but not with single quotes: $test\n');
print "\n";

# Don't forget the custom quote hacks...
print (qq^Any symbol after qq acts as "double-quote":$test\n^);
print (q"Any symbol after q acts as 'single-quote':$test\n");
print "\n";

# Alternative way of declaring a string list of single words...
print qw( first- second- third- nth );
print "\n";

# Indexing lists
print (( "first", "second", "third", "nth" )[1]);
print "\n";
print qw( first- second- third- nth )[-1];
print "\n";
print qw( first- second- third- nth )[(1,2)];
print "\n";

#you can assign one list to another and do tricks with this...
my $first = 1;
my $second = 2;
print (($first, $second), "\n");

#Ranges
print ((1 .. 10),"\n");
print (reverse(1 .. 10),"\n");
print (('c' .. 'j'),"\n");
