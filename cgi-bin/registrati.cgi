#!/usr/bin/perl -w
use XML::LibXML;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use strict;

require "funzioni/static.cgi";

my $page = new CGI;
my $title = "Chi Siamo";
my $keywords = "cantina, Benato, cantina Benato, registrazione, prenotazione, vini, vini in bottiglia";
my $descr = "Registrazione utente al sito della cantina Benato, per poter prenotare online i nostri vini in bottiglia";
&intestazione($page,$title,$keywords,$descr);
&header($page);
&path($page,'<span xml:lang="en">Homepage</span> &#187; Registrati');
&start_container($page);
# if not sessione
   &navigation_notlog($page,"registrati");
# if sessione
#   &navigation_log($page);

print '
         QUA STAMPI IL CONTENUTO DELLA PAGINA< CIOE` L HTML CHE SI TROVA DENTRO IL TAG div.CONTENT
';

&end_container($page);
&footer($page);
