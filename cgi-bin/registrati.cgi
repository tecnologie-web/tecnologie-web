#!/usr/bin/perl -w
use XML::LibXML;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use strict;
use CGI::Session ( '-ip_match' );

require "funzioni/static.cgi";

my $session = CGI::Session->load();

my $page = new CGI;
my $title = "Registrati";
my $keywords = "cantina, Benato, cantina Benato, registrazione, prenotazione, vini, vini in bottiglia";
my $descr = "Registrazione utente al sito della cantina Benato, per poter prenotare online i nostri vini in bottiglia";
&intestazione($page,$title,$keywords,$descr);
&header($page);
&path($page,'<span xml:lang="en">Homepage</span> &#187; Registrati');
&start_container($page);
# if not sessione
if($session->is_empty or $session->is_expired)
{
   my $etichetta = "Form di registrazione al sito";
   my $legend = "Dati accesso al sito";
   my $legend_p = "Dati personali";
   my $etichetta_usr ="Scegli lo username";
   my $etichetta_pass="Scegli la password";
   my $etichetta_confirm="Conferma la password";
   my $etichetta_nome = "Il tuo nome";
   my $etichetta_cognome = "Il tuo cognome";
   my $etichetta_telefono ="Il tuo telefono";
   my $etichetta_obbligatori = "I campi segnati con * sono opzionali";
   &navigation_notlog($page,"registrati"); 
   
   print $page->div({id=>"content"},
                    $page->h2($etichetta),
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
                                                          {for=>"username"},
                                                          $etichetta_usr
                                                          ),
                                             $page->input({id=>"username",
                                                           type=>"text",
                                                           name=>"username",
                                                           size=>"30"}
                                                          ),     
                                             $page->span({id=>"errorUsername",
                                                          class=>"help",
                                                          }
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
                                                          }
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
                                                           size=>"30"}
                                                          ),     
                                             $page->span({id=>"errorNome",
                                                          class=>"help",
                                                          }
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
                                                           size=>"30"}
                                                          ),     
                                             $page->span({id=>"errorSurname",
                                                          class=>"help",
                                                          }
                                                         ),
                                             ),
                                     $page->p(
                                             $page->label(
                                                          {for=>"email"},
                                                          'La tua <span xml:lang="en">email *</span>'
                                                          ),
                                             $page->input({id=>"email",
                                                           type=>"text",
                                                           name=>"email",
                                                           size=>"30"}
                                                          ),     
                                             $page->span({id=>"errorEmail",
                                                          class=>"help",
                                                          }
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
                                                           size=>"30"}
                                                          ),     
                                             $page->span({id=>"errorPhone",
                                                          class=>"help",
                                                          }
                                                         ),
                                             ),
                                    $page->p(
                                             {id=>"hint"},
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
                                                             value=>"Invia"}
                                                            ),
                                            ),
                                    $page->end_form,
                      );
}
else
{
  # if sessione
   &navigation_log($page);

#print '
#         QUA STAMPI IL CONTENUTO DELLA PAGINA< CIOE` L HTML CHE SI TROVA DENTRO IL TAG div.CONTENT
#';
}
&end_container($page);
&footer($page);
print $page->end_html;