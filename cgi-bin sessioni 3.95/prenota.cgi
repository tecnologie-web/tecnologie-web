#!/usr/bin/perl -w
use XML::LibXML;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use CGI::Cookie;
use POSIX qw/strftime/;
use strict;


#creo oggetto CGI
my $pagina = new CGI;
my %cookies=CGI::Cookie->fetch;
if(not($cookies{'CGISESSID'})) { #---->controllo se la sessione è scaduta o non contiene dati
	my $url = "login.cgi";
	print "Location: $url\n\n";
}
else {#----->la sessione è stata caricata correttamente
    #definisco file xml
    my $file = '../data/db.xml';
    my $c=$cookies{'CGISESSID'}->value;
    my $session = CGI::Session->new("driver:File",$c,{Directory=>"temp_session"}); #---->carico la sessione
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
    my $posizione_vino = $pagina->param('posizione');
    my $utente = $session->param("usr");
    #print $utente;print "cucucucucucucu";
    my $data = strftime('%Y-%m-%d',localtime);

    #controllo per verificare che quantità sia un intero > 0
    my $ok = 0;
    if ($quantita =~/^([123456789]+)([\d]*)$/){
       $ok = 1;
    }
    if ($ok == 0){
          print "Location: catalogo.cgi#$posizione_vino\n\n";
          exit;
    }
    #fine controllo

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
    
    #avviso catalogo.cgi che la registrazione è andata a buon fine
    my $registrato = 1;
    $session->param("registrazione",$registrato);
	#redirect
	my $url = "areapersonale.cgi";
	print "Location: $url\n\n";

	exit;
}


