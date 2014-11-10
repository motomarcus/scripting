#!/usr/bin/perl

use 5.010000;

use warnings;
use XML::Parser

 my $team_number = 42;
 my $filename = 'input.txt';
   
  open(my $fh, '<', $filename) or die "cannot open '$filename' $!";

my $found;
while(<$fh>) {
	if(m/^Team (\d+)$/) {
		next if($1 != $team_number);
		$found = 1;
		last;
	}
 }
 die "cannot find 'Team $team_number'" unless($found);