#!/usr/bin/perl -w
use XML::LibXML;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use strict;

require "funzioni/static.cgi";

#print "Content-type: text/html\n\n";

#creo oggetto CGI
my $pagina = new CGI;

#controllo se ci sono dati nella sessione
  #recupero dati sessione
  my $username = $pagina->param('username');
  my $password = $pagina->param('password'); #non servono
  my $confirm_password = $pagina->param('confirm_password');
  my $nome = $pagina->param('nome');
  my $cognome = $pagina->param('cognome');
  my $email = $pagina->param('email');
  my $telefono = $pagina->param('telefono');
  #cripto password e confirm_password
  my $chiave = "ciao";
  my $cryptPass = crypt($chiave,$password);
  my $cryptControlPass = crypt($chiave,$confirm_password);
  #recupero dati errori
  my @err_usr;
  my @err_nome;
  my @err_cogn;
  my @err_mail;
  my @err_tel;
  my @err_pass;
  #recupero dato se ricevuto o no;
  my $spedito = $pagina->param('spedito');
  
  my $prima_volta = 1;  #valore di default 
  if ( $spedito == 1){  #se ho ricevuto i dati porto prima volta a 0
      $prima_volta = 0;
  }  

  if ( $prima_volta == 1){ #stampo la pagina per la prima volta
    my $title = "Registrazione ";
    my $keywords = "cantina, Benato, cantina Benato, login, prenotazione, vini, vini in bottiglia";
    my $descr = "Registrazione utente al sito della cantina Benato, per poter prenotare online i nostri vini in bottiglia";
    &intestazione($pagina,$title,$keywords,$descr);
    &header($pagina);
   &path($pagina,'<span xml:lang="en">Homepage</span> &#187; Login');
  }
