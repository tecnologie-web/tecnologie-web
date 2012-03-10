#! usr/bin/perl
   use CGI;
   use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
   $page= new CGI;
   print $page->header(),
         $page->start_html(-title=>"Specifica vini"),
         $page->p(ciao),
         $page->end_html;

