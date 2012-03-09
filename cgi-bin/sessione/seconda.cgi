#!/usr/bin/perl
  
  # index.pl
  use CGI;
  use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
  use CGI::Session ( '-ip_match' );
  
  $session = CGI::Session->load();
  $q = new CGI;
  $vuoto = null;#"";
  
  if($session->is_expired)#se la sessione è scaduta
  {
      print $q->header(-cache_control=>"no-cache, no-store, must-revalidate");
      print "Your has session expired. Please login again.";
      print "<br/><a href='login.pl>Login</a>";
  }
  elsif($session->is_empty)#se la sessione non contiene dati
  {
      print $q->header(-cache_control=>"no-cache, no-store, must-revalidate");
      print "You have not logged in";
  }
  else #se la sessione contiene parametri validi
  {
      my $campo = $session->param("usr");
      if($campo eq ''){print "dio boia";print length($campo);}
      print $q->header(-cache_control=>"no-cache, no-store, must-revalidate");
      print "<h2>Benvenuto ";
      print $session->param("usr");
      print " ";
      print "<a href='logout.cgi'>Logout";
    
  }
