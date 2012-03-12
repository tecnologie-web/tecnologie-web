#!/usr/bin/perl -w
use XML::LibXML;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
#use strict;

print "Content-type: text/html\n\n";

#creo oggetto CGI
my $pagina = new CGI;

#inizio recupero dei valori passati
my $username = $pagina->param('username');
my $password = $pagina->param('password');
my $nome = $pagina->param('nome');
my $cognome = $pagina->param('cognome');
my $email = $pagina->param('email');
my $telefono = $pagina->param('telefono');
#fine valori passati

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
#my $frammento = "\n<utente>\n<username>$username</username><password>$password</password><nome>$nome</nome><cognome>$cognome</cognome><email>$email</email><telefono>$telefono</telefono></utente>";
$iscritti[0]->appendChild($frammento);
#my $nodo = $parser->parse_balanced_chunk($frammento);
#$iscritti[@iscritti]->appendChild($frammento);
#dichiaro ed apro file di destinazione
my $fileDestinazione = "data.xml";
open(OUT, ">$fileDestinazione") or die("Non riesco ad aprire il file in scrittura");

#aggiungo il frammento creato
#$radice->appendChild($nuovo_elemento);
#my $nelementi = @iscritti;
#$iscritti[$nelementi]->appendChild($frammento);
#$frammento = $radice->appendChild($frammento);
print OUT $doc->toString;
#print $radice;
close (OUT);

#print " n.iscritti=".$nelementi;

#stampe di prova
#print 'usr:'.$username;
#print " pass:".$password;
#print " nome:".$nome;
#print " cognome:".$cognome;
#print " email".$email;
#print " telefono:".$telefono;
#fine stampe di prova
#my $file = 'data.xml';

#my $parser = XML::LibXML->new();

#my $doc = $parser->parse_file($file);
#my $radice= $doc->getDocumentElement; #estrazione radice

#print $radice->toString;

#my $element = $doc->createElement('nuovo');

#$radice->appendChild($element);

#print $->toString;
#open(OUT, ">'$file''");
#$doc->toString(OUT, 1);
