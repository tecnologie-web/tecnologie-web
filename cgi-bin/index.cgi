#!/usr/bin/perl -w

use XML::LibXSLT;
use XML::LibXML;
use CGI;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session;
my $session= CGI::Session->load();
my $fileDati="../data/db.xml";
my $trasformata;
if($session->is_empty or $session->is_expired) 
	{
      $trasformata="../data/homepage_not_log.xsl";
   }
else 
	{
      $trasformata="../data/homepage.xsl";
   }
#creo il parser
my $parser = XML::LibXML->new();

#creo l'oggetto per la trasformata
my $xslt = XML::LibXSLT->new();

#parser dei due documenti
my $doc = $parser->parse_file($fileDati);
my $xslt_doc = $parser->parse_file($trasformata);

#creazione del foglio di trasformazione
my $stylesheet = $xslt->parse_stylesheet($xslt_doc);

#applicazione del foglio di trasformazione
my $risultato = $stylesheet->transform($doc);

#serializzazione
my $nuovaPagina = $risultato->toString;

#invio della pagina al browser
print "Content-Type: text/html\n";
print "Content-Encoding: utf8\n\n";

print $nuovaPagina;
