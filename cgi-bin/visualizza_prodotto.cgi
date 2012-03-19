#!/usr/bin/perl
   use CGI;
   use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
   use XML::LibXML;
   require "funzioni/static.cgi";
   my $db = "../data/db.xml";
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
   &intestazione($page,"Vista dettaglata prodotto",$string,"descrizione");
   &header($page);
   &path($page,'<span xml:lang="en">Homepage</span> &#187; Catalogo Vini &#187; Vista Dettagliata Prodotto');
   &start_container($page);
   &navigation_notlog($page,"catalogo");
   print $page->div({id=>"content"},
                    $page->h2($etichetta[0]->textContent),
                    $page->img({id=>"vino",src=>$immagine[0]->textContent,alt=>""}),
                    $page->div({id=>"cont_descr"},
                              $page->dl(
                                       $page->dt("Tipologia:"),
                                       $page->dd($tipologia[0]->textContent),
                                       $page->dt("Categoria:"),
                                       $page->dd($categoria[0]->textContent),
                                       $page->dt("Stato:"),
                                       $page->dd($stato[0]->textContent),
                                       $page->dt("Uve:"),
                                       $page->dd($uve[0]->textContent),
                                       $page->dt("Provenienza:"),
                                       $page->dd($provenienza[0]->textContent),
                                       $page->dt("Produzione:"),
                                       $page->dd($produzione[0]->textContent),
                                       $page->dt("Altitudine:"),
                                       $page->dd($altitudine[0]->textContent),
                                       $page->dt("Terreno:"),
                                       $page->dd($terreno[0]->textContent),
                                       $page->dt("Densit&agrave piante:"),
                                       $page->dd($densita_p[0]->textContent),
                                       $page->dt("Periodo raccolta:"),
                                       $page->dd($periodoraccolta[0]->textContent),
                                       $page->dt("Vinificazione ed affinamento:"),
                                       $page->dd($vinificazione[0]->textContent),
                                       $page->dt("Gradazione alcolica:"),
                                       $page->dd($gradazione[0]->textContent),
                                       $page->dt("Colore:"),
                                       $page->dd($colore[0]->textContent),
                                       $page->dt("Note di degustazione"),
                                       $page->dd($degustazione[0]->textContent),
                                       $page->dt("Abbinamenti:"),
                                       $page->dd($abbinamenti[0]->textContent),
                                       $page->dt("Temperatura di servizio:"),
                                       $page->dd($temperatura[0]->textContent),
                                       ),
                              $page->a({href=>"catalogo.cgi"},"Torna al catalogo")
                              )
               );
   &end_container($page);
   &footer($page);
   $page->end_html;
