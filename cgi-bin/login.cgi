#!/usr/bin/perl -w
use XML::LibXML;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use strict;

require "funzioni/static.cgi";

print "Content-type: text/html\n\n";

#creo oggetto CGI
my $pagina = new CGI;

#recupero dato se ricevuto o no;
my $spedito = $pagina->param('spedito');
my $prima_volta = 1;  #valore di default 
if ( $spedito == 1){  #se ho ricevuto i dati porto prima volta a 0
    $prima_volta = 0;
}

if ($prima_volta == 1){
   my $title = "Login";
   my $keywords = "cantina, Benato, cantina Benato, login, prenotazione, vini, vini in bottiglia";
   my $descr = "Login utente al sito della cantina Benato, per poter prenotare online i nostri vini in bottiglia";
   &intestazione($pagina,$title,$keywords,$descr);
   &header($pagina);
   &path($pagina,'<span xml:lang="en">Homepage</span> &#187; Login');
   &start_container($pagina);
   &navigation_notlog($pagina,"login");
  
   my $etichetta ="Login al sito";
   my $legend ="I tuoi dati d&apos;accesso";
   my $etichetta_usr ="Il tuo username";
   my $etichetta_pass = "La tua password";
  
   print $pagina->div({id=>"content"},
                      $pagina->h2($etichetta),
                      $pagina->start_form(
                              -id=>"user", 
                              -method=>"post",
                              -action=>"login.cgi"),
                      $pagina->fieldset(
                                        $pagina->legend($legend),
                                        $pagina->p(
                                                   $pagina->label(
                                                                  {for=>"username"},$etichetta_usr),
                                                   $pagina->input({id=>"username",
                                                                   type=>"text",
                                                                   name=>"username",
                                                                   size=>"30"})               
                                                  ),
                                        $pagina->p(
                                                  $pagina->label(
                                                                  {for=>"password"},$etichetta_pass),
                                                   $pagina->input({id=>"password",
                                                                   type=>"password",
                                                                   name=>"password",
                                                                   size=>"30"}),
                                                   $pagina->input({id=>"spedito",
                                                                   type=>"hidden",
                                                                   name=>"spedito",
                                                                   value=>"1"}),
                                                  ),
                                          
                                        ),
                                        $pagina->p({class=>"buttons"},
                                                    $pagina->input(
                                                                   {type=>"reset",
                                                                    value=>"Cancella"}
                                                                  ),
                                                    $pagina->input(
                                                                   {type=>"submit",
                                                                    value=>"Entra"}
                                                                  ),
                                                  ),
                      $pagina->end_form,
                                                  
   ); 

   &end_container($pagina);
   &footer($pagina);
   print $pagina->end_html;
}  
else{
  my $username = $pagina->param('username');
  my $password = $pagina->param('password');
  my $chiave = "ciao";
  my $cryptPass = crypt($chiave,$password);
  #recupero i dati presenti nel database e li confronto con quelli inseriti
  if (&isPresente($username,$cryptPass) == 1){
    print "utente presente";

  }
  else{
    print "utente non presente";
  }
  
#devo effettuare i controlli
}

sub isPresente($){
  my $usr = shift;
  my $pass = shift;
  #vado a leggere il file xml
   my $db = "../data/db.xml";
   my $path ='//utente[username ="'.$usr.'" and password="'.$pass.'"]';
   my $parser = XML::LibXML->new();
   my $doc = $parser->parse_file($db);
   my $file_content = "";
   open(INPUT,$db);
   while(<INPUT>) 
   {
      $file_content = $file_content.$_;
   }
   $file_content =~ s/<dati .+>(.*)<iscritti>/<dati>\1<iscritti>/s;
   my $doc = $parser->parse_string($file_content);
   my $radice = $doc->getDocumentElement();
   return $radice->exists($path);
   #my @username=$usrs[0]->getElementsByTagName('username');
   #my @supporto;
   #my $lung = @usrs;
   #print $lung;
   #for (my $i = 0; $i < $lung ; $i++){
     #my @elemento = $usrs[$i]->getElementsByTagName('username');
   #  my @elemento;
   #  push (@elemento,$usrs[$i]->getElementsByTagName('username'));
   #  push (@elemento,$usrs[$i]->getElementsByTagName('password'));
   #  my $i_usr = $elemento[0]->textContent;
   #  my $i_pass = $elemento[1]->textContent;  
   #  if (($i_usr eq $usr) && ($pass eq $i_pass)){
   #   return 1;
   #  }
   #}
   #return 0;
}
