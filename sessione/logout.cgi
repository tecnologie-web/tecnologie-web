#!/usr/bin/perl
  
  # index.pl
  use CGI;
  use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
  use CGI::Session ( '-ip_match' );
  
  $session = CGI::Session->load();
  $q = new CGI;
  
  print $q->header(-cache_control=>"no-cache, no-store, must-revalidate");
  
  if($session->is_empty){
      print $q->header(-cache_control=>"no-cache, no-store, must-revalidate");
      print "Non dovresti essere qui";
  }
  else{
    #undef($session);
    #$session->set_empty();
    $session->delete();
    #$session->flush();
    #$session->clear();
    #$session->close();
    print "sessione chiusa correttamente";
  }
  
