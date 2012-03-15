#!/usr/bin/perl
   use CGI;
   use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
   $buffer = $ENV{'QUERY_STRING'}; 
   @pairs = split(/&/, $buffer); 
   foreach $pair (@pairs) { 
      ($name, $value) = split(/=/, $pair); 
      $value =~ tr/+/ /; 
      $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg; 
      $name =~ tr/+/ /; 
      $name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C",hex($1))/eg; 
      $input{$name} = $value; 
      } 
   $page= new CGI;
   print $page->header(),
         $page->start_html(-title=>"Specifica vini"),
         $page->p($input{vino}),
         $page->end_html;
