#!/usr/bin/perl -w
use XML::LibXML;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use strict;

print "Content-type: text/html\n\n";

#creo oggetto CGI
my $pagina = new CGI;

#inizio recupero dei valori passati
my $username = $pagina->param('username');
my $password = $pagina->param('password');
my $confirm_password = $pagina->param('confirm_password');
my $nome = $pagina->param('nome');
my $cognome = $pagina->param('cognome');
my $email = $pagina->param('email');
my $telefono = $pagina->param('telefono');
#fine valori passati

#se num_err>0 i campi contengono almeno un errore
my $num_err = 0;
#definizione array errori
my @err_usr;  #username
my @err_pass; #password
my @err_conf; #conferma password
my @err_nome; #nome
my @err_cogn; #cognome
my @err_mail; #email
my @err_tel;  #telefono
#fine array errori

###############################
#TIPI DI ERRORE               #
# 1 : campo contiene < o >    #
# 2 : campo contiene char non #
#     validi o numeri         #


#funzione che cerca l'occorrenza di < o >
sub angolari($){
  my $stringa = shift;
  #if ( $stringa =~ m/</ || $stringa =~ m/>/){
   if ( $stringa =~ /[\<\>]/) {
    return 1;
  }
  else{
     return 0;
  }
}
#fine angolari

#funzione che restituisce 1 se trova occorenze di caratteri non alfabetici
sub not_alpha($){
  my $stringa = shift;
  if( $stringa =~ /^([A-Za-z]+)( [A-Za-z]+)*$/){#se la stringa è così composta ok
    return 0;
  }
  else{#se non lo è
    if ( $stringa =~ /^[A-Za-zèùàòé][a-zA-Z'èùàòé]*$/){#se è nella forma xxx'xxx
      return 0;
    }
    else{
      return 1;
    }
  }
}
#fine non alfabetici

#funzione che riconosce gli ' su nomi e 
#controllo per ogni parametro se presenti angolari
  if(&angolari($username) == 1){
      push(@err_usr,1);
      $num_err++;
  }
  if(&angolari($password) == 1){
      push(@err_pass,1);
      $num_err++;
  }
  if(&angolari($confirm_password) == 1){
      push(@err_conf,1);
      $num_err++;
  }
  if(&angolari($nome) == 1){
      push(@err_nome,1);
      $num_err++;
  }
  if(&angolari($cognome) == 1){
      push(@err_cogn,1);
      $num_err++;
  }
  if(&angolari($email) == 1){
      push(@err_mail,1);
      $num_err++;
  }
  if(&angolari($telefono) == 1){
      push(@err_tel,1);
      $num_err++;
  }
#fine controlli angolari

#controllo se nome contiene caratteri illeciti
if(&not_alpha($nome) == 1){
  push(@err_nome,2);
#  print $num_err;
  $num_err++;
}
#fine controllo

#controllo se cognome contiene caratteri illeciti
#if(&not_alpha($cognome) == 1){
#  push(@err_cogn,2);
#  print $num_err;
#  $num_err++;
#}

#fine controllo

#print $num_err;

#aiuto di rivelazione errori:
#errori sullo username;
print "username= $username errori:"; 
  for (my $i=0; $i<5; $i++){
    print @err_usr[$i]; print " ";
  }
print " <br>";
#errori sul nome:
print "nome = $nome errori: "; #print @err_nome[0];
  for (my $i=0; $i<5; $i++){
    print @err_nome[$i]; print " ";
  }
print " <br>";
#errori sulla password
print "password = $password errori: <br>";
#errori sulla conferma password
print "conferma_password = $confirm_password errori: <br>";
#errori sul cognome
print "cognome = $cognome errori: <br>";
#errori sul telefono
print "telefono = $telefono errori: <br>";
#errori sulla mail
print "email = $email errori: <br>";

if ($num_err>0){
    exit;
}
#definisco file xml
my $file = 'data.xml';

#creazione oggetto parser
my $parser = XML::LibXML->new();

#apertura file e lettura input
my $doc = $parser->parse_file($file);

#estrazione elemento radice
my $radice= $doc->getDocumentElement;
my @iscritti = $radice->getElementsByTagName('iscritti');

#definizione elemento da inserire
my $nuovo_elemento = 
"
    <utente>
      <username>$username</username>
     <password>$password</password>
     <nome>$nome</nome>
     <cognome>$cognome</cognome>
     <email>$email</email>
     <telefono>$telefono</telefono>
    </utente>";



#controllo e creazione di un nuovo nodo
my $frammento = $parser->parse_balanced_chunk($nuovo_elemento);
#appendo il nuovo appena creato
$iscritti[0]->appendChild($frammento);

#definisco il file xml su cui scrivere e lo apro
my $fileDestinazione = "data.xml";
open(OUT, ">$fileDestinazione") or die("Non riesco ad aprire il file in scrittura");
#scrivo effettivamente sul file
print OUT $doc->toString;
#chiudo file
close (OUT);
