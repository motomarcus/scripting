#!/usr/bin/perl

use 5.010000;
use warnings;


 my $team_number = 42;
 my $filename = 'output.txt';
   
  open(my $fh, '>', $filename) or die "cannot open '$filename' $!";
  print $fh "'bollox'".$team_number;
  
  close($fh);
