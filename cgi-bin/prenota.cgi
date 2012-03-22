#!/usr/bin/perl -w
use XML::LibXML;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use POSIX qw/strftime/;
use strict;


#creo oggetto CGI
my $pagina = new CGI;
my $session = CGI::Session->load(); #---->carico la sessione
if($session->is_expired or $session->is_empty) { #---->controllo se la sessione è scaduta o non contiene dati
	print "Content-type: text/html\n\n";
    print "Non sei loggato non puoi prenotare";
}
else {#----->la sessione è stata caricata correttamente
    #definisco file xml
    my $file = '../data/db.xml';

    #creazione oggetto parser
    my $parser = XML::LibXML->new();

    #apertura file e lettura input
    my $doc = $parser->parse_file($file);

    #estrazione elemento radice
    my $radice= $doc->getDocumentElement;
    my @prenotazioni = $radice->getElementsByTagName('prenotazioni');

    #ricavo dati da form
    my $etichetta = $pagina->param('etichetta');
    my $quantita = $pagina->param('quantita');
    my $utente = $session->param('username');
    my $data = strftime('%Y-%m-%d',localtime);

    #definizione elemento da inserire
    my $nuovo_elemento = 
    "
      <commissione>
   		<cliente>".$utente."</cliente>
   		<ordine>".$etichetta."</ordine>
   		<quantita>".$quantita."</quantita>
   		<data>".$data."</data>
   		<evaso>false</evaso>
   	</commissione>
      ";

    #controllo e creazione di un nuovo nodo
    my $frammento = $parser->parse_balanced_chunk($nuovo_elemento);
    #appendo il nuovo appena creato
    $prenotazioni[0]->appendChild($frammento);

    #definisco il file xml su cui scrivere e lo apro
    my $fileDestinazione = "../data/db.xml";
    open(OUT, ">$fileDestinazione") or die("Non riesco ad aprire il file in scrittura");
    #scrivo effettivamente sul file
    print OUT $doc->toString;
    #chiudo file
    close (OUT);

	#redirect
	my $url = "catalogo.cgi";
	print "Location: $url\n\n";

	exit;
}


