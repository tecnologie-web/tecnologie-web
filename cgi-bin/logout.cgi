#!/usr/bin/perl
   use CGI;
   use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
   use CGI::Session ( '-ip_match' );
   use strict;
   my $page = new CGI;
  
   my $session = CGI::Session->load();
   if($session->is_empty)
      {
      my $url = "login.cgi";
      print "Location: $url\n\n";
      }
  else
      {
      $session->delete();
      my $url = "login.cgi";
      print "Location: $url\n\n";
      }
  
