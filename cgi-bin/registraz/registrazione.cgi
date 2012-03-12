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
  if ( $stringa =~ m/</ || $stringa =~ m/>/){
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
  if( $stringa =~ /^([A-Za-z]+)( [A-Za-z]+)*$/){
    return 0;
  }
  else{
    return 1;
  }
}
#fine non alfabetici

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
  print $num_err;
  $num_err++;
}
#fine controllo

#controllo se cognome contiene caratteri illeciti
if(&not_alpha($cognome) == 1){
  push(@err_cognome,2);
  print $num_err;
  $num_err++;
}

#fine controllo
 
#foreach my $errore(@err_nome)
#{
#    print " ";
#    print;
#}
print $num_err;
#my @parametri = ($username, $password, $confirm_password, $nome, $cognome, $email,$telefono);

#my $n_errori = 0;
#controllo se i parametri contengono < o >
#foreach my $elemento(@parametri)
#{
#   if ( $elemento =~ m/</ || $elemento =~ m/>/){
#      $n_errori++;
#   }    
#}

#my $lunghezza = @parametri;
#for(my $i=0; $i < $lunghezza; $i++)
#{
#  if ( @parametri[i] =~ m/</ || @parametri[i] =~ m/>/){
#    print "errore 1 ";
#    #exit;
#  }
#  else
#  {
#    print "ok";
#  }
#}

#devo controllare correttezza dei dati in input
  #PASSWORD#
  #cerco se presente carattere '<'  
#  if ( $password =~ m/</ || $password =~ m/>/) 
# {
#     my $err_pag = "errore.html";
#     print $pagina->redirect($err_pag);
#     exit;
# }
    
  #controllo se le password coincidono
#  my $corretto = 1;
#  if (!($password eq $confirm_password)){
 #   print "non coincidono";
#  }
#fine controlli

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
