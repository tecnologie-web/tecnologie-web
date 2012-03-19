#!/usr/bin/perl -w
use XML::LibXML;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use strict;

my $page = new CGI;
my $title = "Chi Siamo";
my $keywords = "cantina, Benato, descrizione, storia, contatti, orari, vini";
my $descr = "Storia della cantina Benato, i nostri orari di apertura e chiusura, i contatti per telefonarci o scriverci";
&intestazione($page,$title,$keywords,$descr);
&header($page);
&path($page,....);
