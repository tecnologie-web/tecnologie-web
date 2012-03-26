#!/usr/bin/perl

#     Session alla 3.95 
#  Con utilizzo dei cookie
#  aggiornato al 25/03/2012
   
   use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
   use CGI::Session;
   use CGI::Cookie;
   use strict;

   my %cookies=CGI::Cookie->fetch;
   
   if(not($cookies{'CGISESSID'}))
      {
      my $url = "login.cgi";
      print "Location: $url\n\n";
      }
  else
      {
      my $c=$cookies{'CGISESSID'}->value;
      my $session = new CGI::Session->new("driver:File",$c,{Directory=>"temp_session"}); #---->carico la sessione
      $session->delete();
      $cookies{'CGISESSID'}->expires('-1h');
      print "Set-Cookie: $cookies{'CGISESSID'}\n";
      my $url = "index.cgi";
      system("rm temp_session/cgisess_".$c);
      print "Location: $url\n\n";
      }
  
