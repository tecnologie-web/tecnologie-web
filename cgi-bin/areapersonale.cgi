#!/usr/bin/perl -w
use XML::LibXML;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session ( '-ip_match' );
require "funzioni/trasformazioni_xml.cgi";
require "funzioni/static.cgi";

use strict;



#creo oggetto CGI
my $page = new CGI;
my $session = CGI::Session->load(); #---->carico la sessione
if($session->is_expired or $session->is_empty) { #---->controllo se la sessione è scaduta o non contiene dati
    print "Content-type: text/html\n\n";
    print "Non sei loggato non puoi vedere la sezione personale dell'utente";
}
else {#----->la sessione è stata caricata correttamente
   
   #carico il file db.xml
   my $db = "../data/db.xml";
   my $path = 'prenotazioni/commissione[cliente="'.$session->param("usr").'" and evaso="false"]';
   #creo  il parser XML
   my $parser = XML::LibXML->new();
   
   #tolgo i ns del file per riuscire ad utilizzare la funzione findnodes()
   my $doc = $parser->parse_string(&togli_ns($db));
   
   my $radice = $doc->getDocumentElement();
   
   my @prenotazioni = $radice->findnodes($path);
   
   my $lung = @prenotazioni;

   my $title = "Area Personale";
   my $keywords = "cantina, Benato, cliente, area personale, vini prenotati";
   my $descr = "Visualizza l'area personale del cliente, mostrando i vini prenotati";
   &intestazione($page,$title,$keywords,$descr);
   &header($page);
   &path($page,'<span xml:lang="en">Homepage</span> &#187; Area Personale');
   &start_container($page);
   &navigation_log($page,"areapersonale");
      print $page->start_div({id=>"content"});
      print $page->h2("Area personale cliente");
      print $page->start_ul({id=>"nav_cliente"});
      print $page->li($page->a({href=>"cliente.html"},"I miei dati personali"));
      print $page->li({-id=>"here"},"Le mie prenotazioni");
      print $page->end_ul;
      print $page->start_div({id=>"data_cliente"});
      print $page->start_ul;
      if($lung==0)
         {
            print $page->li({id=>"attention"},
                           "Non hai ancora effettuato prenotazioni! Consulta il nostro ",
                           $page->a({href=>"catalogo.cgi"},"catalogo vini"));
         }
      else
         {
         for(my $i=0;$i<$lung;$i++)
            {
               my @quantita = $prenotazioni[$i]->getElementsByTagName("quantita");
               my @tipo = $prenotazioni[$i]->getElementsByTagName("ordine");
               my @data = $prenotazioni[$i]->getElementsByTagName("data");
               my @dati=split("-",$data[0]->firstChild()->toString(1,1));
               print $page->start_li;
               print $page->start_dl;
               print $page->dt("Ordine numero :");
               print $page->dd($i+1);
               print $page->dt("Quantità :");
               print $page->dd($quantita[0]->firstChild()->toString(1,1));
               print $page->dt("Tipologia :");
               print $page->dd($tipo[0]->firstChild()->toString(1,1));
               print $page->dt("Ordinato il :");
               print $page->dd($dati[2],"/",$dati[1],"/",$dati[0]);
               print $page->end_dl;
               print $page->end_li;
            }
         }
         
      print $page->end_ul;
      print $page->end_div;
      print $page->end_div;
    &end_container($page);
    &footer($page);
    print $page->end_html;

}


