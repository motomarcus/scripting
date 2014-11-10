#!/usr/bin/perl
use strict;
use warnings;

#Look at lists.pl if the syntax here needs clarifying

#Array is the variable type to which we can assign a list
my @days = qw( Monday Tuesday Wednesday Thursday Friday Saturday Sunday);
print (@days, "\n");
print ("@days\n");

#what happens if I assign a list to a SCALAR variable?
my $days = @days;
print ($days, "\n");
print (scalar @days,"\n");

my @numericArray = (1 .. 9);
print @numericArray, "\n";
print (($numericArray[1]),  "\n"); # NOTE the use of $ for accessing array element
print (($days[2]),  "\n");  # NOTE the use of $ for accessing array element

my $wed = $days[2];
print "Midweek is $wed \n";

my $singleNumber  = $numericArray[2]; # NOTE the use of $ for accessing array element
print "Single number is $singleNumber \n";

my @midWeekDays = @days[2 .. 4];
print "Midweek days are: @midWeekDays \n";




