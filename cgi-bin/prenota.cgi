#!/usr/bin/perl -w
use XML::LibXML;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use strict;

print "Content-type: text/html\n\n";

#creo oggetto CGI
my $pagina = new CGI;

# if sessione aperta
my $vino = $pagina->param('etichetta');
my $quantita = $pagina->param('quantita');

