#!/usr/bin/perl
use warnings;
use strict;

my @stuff = ('a', 'b', 'c', 'd');

push(@stuff, 'e');

@stuff += 'f';

print(@stuff,"\n");