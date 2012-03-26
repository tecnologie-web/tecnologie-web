#!/usr/bin/perl -w
use XML::LibXML;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use CGI::Cookie;
use strict;


require "funzioni/static.cgi";
require "funzioni/controlli.cgi";
my %cookies=CGI::Cookie->fetch;


my $title = "Registrati";
my $keywords = "cantina, Benato, cantina Benato, registrazione, prenotazione, vini, vini in bottiglia";
my $descr = "Registrazione utente al sito della cantina Benato, per poter prenotare online i nostri vini in bottiglia";

# if not sessione
if(not($cookies{'CGISESSID'}))
{
  my $page = new CGI;
  #recupero dati sessione
  &intestazione($page,$title,$keywords,$descr);
  &header($page);
  &path($page,'<span xml:lang="en">Homepage</span> &#187; Registrati');
  &start_container($page);
 
  my $username = $page->param('username');
  my $password = $page->param('password'); #non servono
  my $confirm_password = $page->param('confirm_password');
  my $nome = $page->param('nome');
  my $cognome = $page->param('cognome');
  my $email = $page->param('email');
  my $telefono = $page->param('telefono');
  #cripto password e confirm_password
  my $chiave = "ciao";
  my $cryptPass = crypt($chiave,$password);
  my $cryptControlPass = crypt($chiave,$confirm_password);
  
  #recupero dato se ricevuto o no;
  my $spedito = $page->param('spedito');
  
#fine recupero dati

#definizione array errori
  my @err_usr;
  my @err_nome;
  my @err_cogn;
  my @err_mail;
  my @err_tel;
  my @err_pass;
#fine array  
  my $prima_volta = 1;  #valore di default 
  if ( $spedito == 1){  #se ho ricevuto i dati porto prima volta a 0
      $prima_volta = 0;
  }
#  if ($prima_volta == 0){print "ma riciao";}  
   
   &navigation_notlog($page,"registrati"); 
   if ($prima_volta == 1){
    &printP($page,-1);#passo num_err= -1
   }
   else{ #non è la prima volta e devo effettuare i controlli
      my $num_err = 0;
   #tutti obbligatori devono venir riempiti
   if(&not_vuoto($username) == 1){
      push(@err_usr,6);
      $num_err++;
   }
   if(&not_vuoto($password) == 1){
      push(@err_pass,6);
      $num_err++;
   }
   if(&not_vuoto($nome) == 1){
      push(@err_nome,6);
      $num_err++;
   }
   if(&not_vuoto($cognome) == 1){
      push(@err_cogn,6);
      $num_err++;
   }
   if(&not_vuoto($telefono) == 1){
      push(@err_tel,6);
      $num_err++;
   }
   #controllo per ogni parametro se presenti angolari
    if(&angolari($username) == 1){
      push(@err_usr,1);
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
    
    #controllo che i campi siano nei formati corretti
    if(&not_numbchar($username) == 1){
      push(@err_usr,2);
      $num_err++;
    }
    if(&not_alpha($nome) == 1){
      push(@err_nome,2);
      $num_err++;
    }
    if(&not_alpha($cognome) == 1){
      push(@err_cogn,2);
      $num_err++;
    }
    if(&control_mail($email) == 1){
      push(@err_mail,3);
      $num_err++;
    }
    if(&control_numb($telefono) == 1){
      push(@err_tel,2);
      $num_err++;
    }
    if(!($cryptPass eq $cryptControlPass)){
      push(@err_pass,4);
      $num_err++;
    }
    
    #if username è già presente num err ++
    if (&isPresente($username)){
      push(@err_usr,5);
      $num_err++;
    }
    #fine campi corretti
     my $e_usr = &get_errore(@err_usr[0]);
     my $e_nome = &get_errore(@err_nome[0]);
     my $e_cogn = &get_errore(@err_cogn[0]);
     my $e_mail = &get_errore(@err_mail[0]);
     my $e_tel = &get_errore(@err_tel[0]);
     my $e_pass = &get_errore(@err_pass[0]);
     &printP($page,$num_err,$e_usr,$e_nome,$e_cogn,$e_mail,$e_tel,$e_pass,$username,$nome,$cognome,$email,$telefono);
     
     
    if ($num_err == 0){#print "DATI CORRETTI";
      #definisco file xml
      my $file = '../data/db.xml';

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
         <password>".$cryptPass."</password>
         <nome>$nome</nome>
         <cognome>$cognome</cognome>
         <email>$email</email>
         <telefono>$telefono</telefono>
        </utente>
        ";

      #controllo e creazione di un nuovo nodo
      my $frammento = $parser->parse_balanced_chunk($nuovo_elemento);
      #appendo il nuovo appena creato
      $iscritti[0]->appendChild($frammento);

      #definisco il file xml su cui scrivere e lo apro
      my $fileDestinazione = "../data/db.xml";
      open(OUT, ">$fileDestinazione") or die("Non riesco ad aprire il file in scrittura");
      #scrivo effettivamente sul file
      print OUT $doc->toString;
      #chiudo file
      close (OUT);
      
      #my $url = "login.cgi";
      #print "Location: $url\n\n";
      #redirect
      #print $page->header(-location=>"login.cgi");
    }
   }
   &end_container($page);
   &footer($page);
   print $page->end_html;

}
else
{
  my $url = "areapersonale.cgi";
  print "Location: $url\n\n";
}



sub printP($){
   #stampa pagina
   my $page = shift;
   my $etichetta = "Form di registrazione al sito";
   my $legend = "Dati accesso al sito";
   my $legend_p = "Dati personali";
   my $etichetta_usr ="Scegli lo username";
   my $etichetta_pass="Scegli la password";
   my $etichetta_confirm="Conferma la password";
   my $etichetta_nome = "Il tuo nome";
   my $etichetta_cognome = "Il tuo cognome";
   my $etichetta_telefono ="Il tuo telefono";
   my $etichetta_obbligatori = "(I campi segnati con (*) sono opzionali)"; 
  
   my $num_err = shift;
   my $e_usr = shift;# &get_errore(@err_usr[0]);
   my $e_nome = shift;#&get_errore(@err_nome[0]);
   my $e_cogn = shift;#&get_errore(@err_cogn[0]);
   my $e_mail = shift;#&get_errore(@err_mail[0]);
   my $e_tel = shift;#&get_errore(@err_tel[0]);
   my $e_pass = shift;#&get_errore(@err_pass[0]);
   my $username = shift;
   my $nome = shift;
   my $cognome = shift;
   my $email = shift;
   my $telefono = shift;
   
   my $messaggio;
   if ($num_err == 0){
      $messaggio = "Registrazione riuscita! Entra subito al <a href=\"login.cgi\">Login</a>";
      $username = "";
      $nome = "";
      $cognome = "";
      $email = "";
      $telefono ="";
   }
   elsif ($num_err > 0){
      $messaggio = "Registrazione non riuscita! ";
   }
     
 print $page->div({id=>"content"},
                    $page->h2($etichetta),
                    $page->h3(
                                  {id=>"result"},
                                  $messaggio
                                  ),
                    $page->start_form(
                              -id=>"user", 
                              -method=>"post",
                              -action=>"registrati.cgi",
                              -onsubmit=>"return validateRegistration();",
                          ),
                    $page->fieldset({id=>"site"},
                                    $page->legend($legend),
                                    $page->p(
                                             $page->label(
                                                          {for=>"usename"},
                                                          $etichetta_usr
                                                          ),
                                             $page->input({id=>"username",
                                                           type=>"text",
                                                           name=>"username",
                                                           size=>"30",
                                                           value=>"$username"}
                                                          ),     
                                             $page->span({id=>"errorUsername",
                                                          class=>"help",
                                                          },"$e_usr"
                                                         ),
                                             ),
                                    $page->p(
                                             $page->label(
                                                          {for=>"password"},
                                                          $etichetta_pass
                                                          ),
                                             $page->input({id=>"password",
                                                           type=>"password",
                                                           name=>"password",
                                                           size=>"30"}
                                                          ),     
                                             $page->span({id=>"errorPassword",
                                                          class=>"help",
                                                          },"$e_pass"
                                                         ),                                        
                                            ),
                                    $page->p(
                                             $page->label(
                                                          {for=>"confirm_password"},
                                                          $etichetta_confirm
                                                          ),
                                             $page->input({id=>"confirm_password",
                                                           type=>"password",
                                                           name=>"confirm_password",
                                                           size=>"30"}
                                                          ),     
                                             $page->span({id=>"errorCPassword",
                                                          class=>"help",
                                                          }
                                                         ),                                        
                                            ),
                          ),
                    $page->fieldset({id=>"personal"},
                                    $page->legend($legend_p),
                                    $page->p(
                                             $page->label(
                                                          {for=>"nome"},
                                                          $etichetta_nome
                                                          ),
                                             $page->input({id=>"nome",
                                                           type=>"text",
                                                           name=>"nome",
                                                           value=>"$nome",
                                                           size=>"30"}
                                                          ),
                                             $page->input(
                                                          {
                                                            name=>"spedito",
                                                            type=>"hidden",
                                                            value=>"1",
                                                          }
                                                         ),
                                             $page->span({id=>"errorNome",
                                                          class=>"help",
                                                          },"$e_nome"
                                                         ),
                                             ),
                                    $page->p(
                                             $page->label(
                                                          {for=>"cognome"},
                                                          $etichetta_cognome
                                                          ),
                                             $page->input({id=>"cognome",
                                                           type=>"text",
                                                           name=>"cognome",
                                                           value=>"$cognome",
                                                           size=>"30"}
                                                          ),     
                                             $page->span({id=>"errorSurname",
                                                          class=>"help",
                                                          },"$e_cogn"
                                                         ),
                                             ),
                                     $page->p(
                                             $page->label(
                                                          {for=>"email"},
                                                          'La tua <span xml:lang="en">email (*)</span>'
                                                          ),
                                             $page->input({id=>"email",
                                                           type=>"text",
                                                           name=>"email",
                                                           value=>"$email",
                                                           size=>"30"}
                                                          ),     
                                             $page->span({id=>"errorEmail",
                                                          class=>"help",
                                                          },"$e_mail"
                                                         ),
                                             ),         
                                    $page->p(
                                             $page->label(
                                                          {for=>"telefono"},
                                                          $etichetta_telefono
                                                          ),
                                             $page->input({id=>"telefono",
                                                           type=>"text",
                                                           name=>"telefono",
                                                           value=>"$telefono",
                                                           size=>"30"}
                                                          ),     
                                             $page->span({id=>"errorPhone",
                                                          class=>"help",
                                                          },"$e_tel"
                                                         ),
                                             ),
                                    $page->p({id=>"hint"},
                                             $etichetta_obbligatori
                                            ),
                                    ),
                                    $page->p({class=>"buttons"},
                                             $page->input(
                                                            {type=>"reset",
                                                             value=>"Cancella"}
                                                            ),
                                             $page->input(
                                                            {type=>"submit",
                                                             value=>"Invia",
                                                            onclick=>"return validateRegistration();"}
                                                            ),
                                            ),
                                    $page->end_form,
                      );
    
}


