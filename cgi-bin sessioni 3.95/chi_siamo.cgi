#!/usr/bin/perl -w
use XML::LibXML;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use CGI::Cookie;
use strict;

require "funzioni/static.cgi";

my $page = new CGI;
my %cookies=CGI::Cookie->fetch;
my $title = "Chi Siamo";
my $keywords = "cantina, Benato, descrizione, storia, contatti, orari, vini";
my $descr = "Storia della cantina Benato, i nostri orari di apertura e chiusura, i contatti per telefonarci o scriverci";
&intestazione($page,$title,$keywords,$descr);
&header($page);
&path($page,'<span xml:lang="en">Homepage</span> &#187; Chi Siamo');
&start_container($page);


if(not($cookies{'CGISESSID'})) { #---->controllo se la sessione è scaduta o non contiene dati
   &navigation_notlog($page,"chisiamo");
}
else {#----->la sessione è stata caricata correttamente
   &navigation_log($page,"chisiamo");
}
print '
<div id="content">
            <h2><a name="top"></a>Chi siamo</h2>
            <div id="chisiamo">
               <img src="../images/vigneto.jpg" alt="Il vigneto dell&apos;azienda Cantina Benato" />
               <p>
                  <span class="firstLetter">L</span>a <strong>Cantina Benato</strong> nasce nel cuore dei <strong>Colli Euganei</strong> in provincia di Padova e si dedica alla produzione di vino da   più <strong>generazioni</strong>.
               </p>
               <p>
                  Il prodotto, di <strong>qualità</strong>, nasce da un&apos;attenta coltivazione della vigna, da una curata raccolta dell&apos;uva, da una successiva lavorazione effettuata con moderne tecnologie secondo i dettami della <strong>tradizione</strong> e avvalorata da una antica passione e cultura della viti-vinificazione.
               </p>
               <p>
                  La non eccessiva estensione consente la gestione quasi famigliare delle lavorazioni dei vigneti e la trasformazione dell&apos;uva in vino, così da garantire al consumatore un <strong>elevato standard qualitativo</strong>. <br /> Abbiamo quindi la possibilità di offrire un ventaglio di varietà molto ampio, così da poter incontrare il più possibile il gusto del cliente.
               </p>
            </div>
            
            <a class="internal_nav" href="#top">Torna su &#9650;</a>
            
            <h2>I nostri contatti</h2>
            <ul class="address">
               <li>Cantina Benato di Benato Romeo e figlio</li>
               <li>Via Monte Castellaro, 176</li>
               <li>35030 Boccon di Vo&apos; (PD)</li>
               <li>Tel e fax 049 9940255 </li>
               <li>P.I. 003940670288</li>
            </ul>
            
            <a class="internal_nav" href="#top">Torna su &#9650;</a>
            
            <h2>I nostri orari</h2>
            <table id="orari" summary="Orari di apertura di Cantina Benato: Lunedì mattina dalle 9 alle 12 e 30, Lunedì pomeriggio dalle 14 e 30 alle 19, Martedì mattina dalle 9 alle 12 e 30, Martedì pomeriggio dalle 14 e 30 alle 19, Mercoledì mattina dalle 9 alle 12 e 30, Mercoledì pomeriggio dalle 14 e 30 alle 19, Giovedì mattina dalle 9 alle 12 e 30, Giovedì pomeriggio dalle 14 e 30 alle 19, Venerdì mattina dalle 9 alle 12 e 30, Venerdì pomeriggio dalle 14 e 30 alle 19, Sabato mattina dalle 9 alle 12 e 30, Sabato pomeriggio dalle 14 e 30 alle 19, Domenica dalle 10 alle 18">
            <caption>Orari di apertura della Cantina Benato</caption>
               <thead>
                  <tr>
                     <th></th>
                     <th id="c2" abbr="Lun" scope="col">Lunedì</th>
                     <th id="c3" abbr="Mar" scope="col">Martedì</th>
                     <th id="c4" abbr="Mer" scope="col">Mercoledì</th>
                     <th id="c5" abbr="Gio" scope="col">Giovedì</th>
                     <th id="c6" abbr="Ven" scope="col">Venerdì</th>
                     <th id="c7" abbr="Sab" scope="col">Sabato</th>
                     <th id="c8" abbr="Dom" scope="col">Domenica</th>
                  </tr>
               </thead>
               <tbody>
                  <tr>
                     <th id="r2" abbr="Matt" scope="row">Mattina</th>
                     <td headers="r2 c2">9:00 - 12:30</td>
                     <td headers="r2 c3">9:00 - 12:30</td>
                     <td headers="r2 c4">9:00 - 12:30</td>
                     <td headers="r2 c5">9:00 - 12:30</td>
                     <td headers="r2 c6">9:00 - 12:30</td>
                     <td headers="r2 c7">9:00 - 12:30</td>
                     <td headers="r2 r3 c8" rowspan="2">10:00 - 18:00</td>
                  </tr>
                  <tr>
                     <th id="r3" abbr="Pom" scope="row">Pomeriggio</th>
                     <td headers="r3 c2">14:30 - 19:00</td>
                     <td headers="r3 c3">14:30 - 19:00</td>
                     <td headers="r3 c4">14:30 - 19:00</td>
                     <td headers="r3 c5">14:30 - 19:00</td>
                     <td headers="r3 c6">14:30 - 19:00</td>
                     <td headers="r3 c7">14:30 - 19:00</td>
                  </tr>
               </tbody>
            </table>
            
            <a class="internal_nav" href="#top">Torna su &#9650;</a>
            
         </div>  <!--content-->
';

&end_container($page);
&footer($page);
print $page->end_html;
