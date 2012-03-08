#!/usr/bin/perl
  
  # login.pl
  use CGI;
  use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
  use CGI::Session;# ( '-ip_match' );
  
  $q = new CGI;
  
  $usr = $q->param('usr');
  $pwd = $q->param('pwd');
  
  if($usr ne '')
  {
      # process the form
      if($usr eq "catte" and $pwd eq "pass")
      {
          $session = new CGI::Session();
          $session->param("usr",$usr);
          print $session->header(-location=>'seconda.cgi');
      }
      else
      {
          print $q->header(-type=>"text/html",-location=>"errore.html");
      }
  }
  #elsif($q->param('action') eq 'logout')
  #{
  #    $session = CGI::Session->load() or die CGI::Session->errstr;
  #    $session->delete();
  #    print $session->header(-location=>'login.pl');
  #}
  else
  {
      $page = new CGI;
      print $page->header,
      $page->start_html(
       # inizio pagina HTML
       -title => 'Sessione',
      ),
      $page->p( "
          <form method=\"post\">
          Username: <input type=\"text\" name=\"usr\">
  
          Password: <input type=\"password\" name=\"pwd\">
  
  
          <input type=\"submit\">
     ")
  
  }
