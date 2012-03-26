#!/usr/bin/perl -w

#     Session alla 3.95 
#  Con utilizzo dei cookie
#  aggiornato al 25/03/2012

use XML::LibXML;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use CGI::Cookie;
require "funzioni/trasformazioni_xml.cgi";
require "funzioni/static.cgi";
use strict;



#creo oggetto CGI
my $page = new CGI;
my %cookies=CGI::Cookie->fetch;

if(not($cookies{'CGISESSID'})) { #---->controllo se la sessione è scaduta
   my $url = "login.cgi";
   print "Location: $url\n\n";
}
else {#----->la sessione è stata caricata correttamente
   my $c=$cookies{'CGISESSID'}->value;
   my $session = CGI::Session->new("driver:File",$c,{Directory=>"temp_session"}); #---->carico la sessione
   
   #carico il file db.xml
   my $db = "../data/db.xml";
   
   #creo  il parser XML
   my $parser = XML::LibXML->new();
   
   #tolgo i ns del file per riuscire ad utilizzare la funzione findnodes()
   my $doc = $parser->parse_string(&togli_ns($db));
   
   my $radice = $doc->getDocumentElement();
   my $path = 'prenotazioni/commissione[cliente="'.$session->param("usr").'" and evaso="false"]';
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
      print $page->h2("Area personale cliente: Prenotazioni effetuate");
      if($session->param("registrazione"))
         {
         print $page->h3("Prenotazione Avvenuta con successo!");
         $session->clear(["registrazione"]);
         }
      print $page->start_div({id=>"data_cliente"});
      print $page->start_ul;
      if($lung==0)
         {
            print $page->li({id=>"attention"},
                           "Non hai ancora effettuato prenotazioni!<br /><br /> Consulta il nostro ",
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


