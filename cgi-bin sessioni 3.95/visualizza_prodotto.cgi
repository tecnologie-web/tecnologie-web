#!/usr/bin/perl
   use CGI;
   use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
   use XML::LibXML;
   use CGI::Cookie;
   require "funzioni/static.cgi";
   require "funzioni/trasformazioni_xml.cgi";
   
   my %cookies=CGI::Cookie->fetch;
   my $db = "../data/db.xml";
   my $parser = XML::LibXML->new();
   my $doc = $parser->parse_file($db);
   my $doc = $parser->parse_string(&togli_ns($db));
   
   my $radice = $doc->getDocumentElement();
   
   #ricavo il valore dell'etichetta passata tramite get
   
   $buffer = $ENV{'QUERY_STRING'};
   @pairs = split(/&/, $buffer); 
   foreach $pair (@pairs) { 
      ($name, $value) = split(/=/, $pair); 
      $value =~ tr/+/ /; 
      $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg; 
      $name =~ tr/+/ /; 
      $name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C",hex($1))/eg; 
      $input{$name} = $value; 
      }
   #prelievo dei dati dal file XML
   my $path ='//vino[etichetta="'.$input{vino}.'"]';
if($radice->exists($path))
      {
      my @vini = $radice->findnodes($path);
      my @etichetta=$vini[0]->getElementsByTagName('etichetta');
      my @immagine=$vini[0]->getElementsByTagName('immagine');
      my @tipologia=$vini[0]->getElementsByTagName('tipologia');
      my @categoria=$vini[0]->getElementsByTagName('categoria');
      my @stato=$vini[0]->getElementsByTagName('stato');
      my @uve=$vini[0]->getElementsByTagName('uve');
      my @provenienza=$vini[0]->getElementsByTagName('provenienza');
      my @produzione=$vini[0]->getElementsByTagName('produzione');
      my @altitudine=$vini[0]->getElementsByTagName('altitudine');
      my @terreno=$vini[0]->getElementsByTagName('terreno');
      my @densita_p=$vini[0]->getElementsByTagName('densita_p');
      my @periodoraccolta=$vini[0]->getElementsByTagName('periodoraccolta');
      my @vinificazione=$vini[0]->getElementsByTagName('vinificazione');
      my @gradazione=$vini[0]->getElementsByTagName('gradazione');
      my @colore=$vini[0]->getElementsByTagName('colore');
      my @degustazione=$vini[0]->getElementsByTagName('degustazione');
      my @abbinamenti=$vini[0]->getElementsByTagName('abbinamenti');
      my @temperatura=$vini[0]->getElementsByTagName('temperatura');
      my @prezzo=$vini[0]->getElementsByTagName('prezzo');
      my $page = new CGI;
      &intestazione($page,"Vista dettagliata prodotto",$string,"descrizione");
      &header($page);
      &path($page,'<span xml:lang="en">Homepage </span> &#187; Catalogo Vini &#187; Vista Dettagliata Prodotto');
      &start_container($page);
      if(not($cookies{'CGISESSID'}))
         {
         &navigation_notlog($page,"catalogo");
         }
      else
         {
         &navigation_log($page,"catalogo");
         }
      print $page->div({id=>"content"},
                       $page->h2($etichetta[0]->textContent),
                       $page->img({id=>"vino",src=>$immagine[0]->textContent,alt=>""}),
                       $page->div({id=>"cont_descr"},
                                 $page->dl(
                                          $page->dt("Tipologia:"),
                                          $page->dd($tipologia[0]->getFirstChild()->toString(1,1)),
                                          $page->dt("Categoria:"),
                                          $page->dd($categoria[0]->getFirstChild()->toString(1,1)),
                                          $page->dt("Stato:"),
                                          $page->dd($stato[0]->getFirstChild()->toString(1,1)),
                                          $page->dt("Uve:"),
                                          $page->dd($uve[0]->getFirstChild()->toString(1,1)),
                                          $page->dt("Provenienza:"),
                                          $page->dd($provenienza[0]->getFirstChild()->toString(1,1)),
                                          $page->dt("Produzione:"),
                                          $page->dd($produzione[0]->getFirstChild()->toString(1,1)),
                                          $page->dt("Altitudine:"),
                                          $page->dd($altitudine[0]->getFirstChild()->toString(1,1)),
                                          $page->dt("Terreno:"),
                                          $page->dd($terreno[0]->getFirstChild()->toString(1,1)),
                                          $page->dt("Densit&agrave piante:"),
                                          $page->dd($densita_p[0]->getFirstChild()->toString(1,1)),
                                          $page->dt("Periodo raccolta:"),
                                          $page->dd($periodoraccolta[0]->getFirstChild()->toString(1,1)),
                                          $page->dt("Vinificazione ed affinamento:"),
                                          $page->dd($vinificazione[0]->getFirstChild()->toString(1,1)),
                                          $page->dt("Gradazione alcolica:"),
                                          $page->dd($gradazione[0]->getFirstChild()->toString(1,1)),
                                          $page->dt("Colore:"),
                                          $page->dd($colore[0]->getFirstChild()->toString(1,1)),
                                          $page->dt("Note di degustazione :"),
                                          $page->dd($degustazione[0]->getFirstChild()->toString(1,1)),
                                          $page->dt("Abbinamenti:"),
                                          $page->dd($abbinamenti[0]->getFirstChild()->toString(1,1)),
                                          $page->dt("Temperatura di servizio:"),
                                          $page->dd($temperatura[0]->getFirstChild()->toString(1,1)),
                                          ),
                                 $page->a({href=>"catalogo.cgi"},"Torna al catalogo")
                                 )
                  );
      &end_container($page);
      &footer($page);
      print $page->end_html;
   }
else
   {
   my $url = "catalogo.cgi";
   print "Location: $url\n\n";
   }
