#!/usr/bin/perl
sub intestazione($)
{
my $pagina = shift;
my $title = shift;
my $key = shift;
my $description=shift;
print  $pagina->header(-charset=>"UTF-8"),
       $pagina->start_html (-title=>$title." ~ Cantina Benato",
                           -dtd=>['-//W3C//DTD XHTML 1.0 Strict//EN' ,'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd'],
                           -meta => {'language' => 'it', 
                                    'author' => 'Giacomo Cattelan, Alessandro Cornaglia, Riccardo De Stefani, Jorge Sotomayor',
                                    'description'=>$description,
                                    'keyword'=>$key},
                           -style=>[{-src=>'../css/screen/main.css',-media=>'screen'},{-src=>'../css/print/main.css',-media=>'print'}],
                           -lang => it
                           )
}
sub header($)
{
my $page = shift;
print $page->div({id=>"header"},
                     $page->img({src=>"../images/logo.png",width=>"260px",alt=>""}),
                     $page->h1("Cantina Benato"),
                     $page->p("Premiata cantina di Benato Romeo e figlio, dal 1960"),
                     $page->div({class=>"clear"},""),
                     )
}
sub path($)
{
my $pagina = shift;
my $path = shift;
print $pagina->div({id=>"path"},
                  "Ti trovi in :",
                  $path            
                  )
}
sub start_container($)
{
my $pagina = shift;
print $pagina->start_div({id=>"container"})
}
sub end_container($)
{
my $pagina = shift;
print $pagina->end_div
}
sub navigation_notlog($)
{
my $page =shift;
my $current=shift;
print $page->a({class=>"nav_help",href=>"#content"},"");
print $page->start_div({id=>"navigation"});
                 print $page->start_ul();
                  if($current eq "homepage")
                     {
                     print $page->li({class=>"homepage",id=>"here"},"Homepage");
                     }
                  else
                     {
                     print $page->li({class=>"homepage"},
                               $page->a({tabindex=>"1",accesskey=>"h",href=>"index.cgi"},
                               '<span xml:lang="en">Homepage</span>')
                              );
                     }
                  if($current eq "catalogo")
                     {
                     print $page->li({class=>"catalogo",id=>"here"},"Catalogo Vini");
                     }
                  else
                     {
                     print $page->li({class=>"catalogo"},
                                    $page->a({tabindex=>"2",accesskey=>"c",href=>"chi_siamo.cgi"},
                                    "Catalogo")
                              );
                     }
                  if($current eq "chisiamo")
                     {
                     print $page->li({class=>"chisiamo",id=>"here"},"Chi Siamo");
                     }
                  else
                     {
                     print $page->li({class=>"chisiamo"},
                                    $page->a({tabindex=>"3",accesskey=>"s",href=>"chi_siamo.cgi"},
                                    "Chi Siamo")
                              );
                     }
                  if($current eq "registrati")
                     {
                     print $page->li({class=>"registrati",id=>"here"},"Registati");
                     }
                  else
                     {
                     print $page->li({class=>"registrati"},
                              $page->a({tabindex=>"4",accesskey=>"r",href=>"registrati.cgi"},
                                       "Registrati")
                              );
                     }
                   if($current eq "login")
                     {
                     print $page->li({class=>"login",id=>"here"},'<span xml:lang="en">Login</span>');
                     }
                  else
                     {
                      print $page->li({class=>"login"},
                                    $page->a({tabindex=>"4",accesskey=>"l",href=>"login.cgi"},
                                             '<span xml:lang="en">Login</span>')
                                 );      
                     }  
print $page->end_ul;
print $page->end_div;
}
sub navigation_log($)
{
my $page =shift;
my $current=shift;
print $page->a({class=>"nav_help",href=>"#content"},"");
print $page->start_div({id=>"navigation"});
                 print $page->start_ul();
                  if($current eq "homepage")
                     {
                     print $page->li({class=>"homepage",id=>"here"},"Homepage");
                     }
                  else
                     {
                     print $page->li({class=>"homepage"},
                               $page->a({tabindex=>"1",accesskey=>"h",href=>"index.cgi"},
                               '<span xml:lang="en">Homepage</span>')
                              );
                     }
                  if($current eq "catalogo")
                     {
                     print $page->li({class=>"catalogo",id=>"here"},"Catalogo Vini");
                     }
                  else
                     {
                     print $page->li({class=>"catalogo"},
                                    $page->a({tabindex=>"2",accesskey=>"c",href=>"catalogo.cgi"},
                                    "Catalogo")
                              );
                     }
                  if($current eq "chisiamo")
                     {
                     print $page->li({class=>"chisiamo",id=>"here"},"Chi Siamo");
                     }
                  else
                     {
                     print $page->li({class=>"chisiamo"},
                                    $page->a({tabindex=>"3",accesskey=>"s",href=>"chi_siamo.cgi"},
                                    "Chi Siamo")
                              );
                     }
                   if($current eq "logout")
                     {
                     print $page->li({class=>"logout",id=>"here"},'<span xml:lang="en">Logout</span>');
                     }
                  else
                     {
                      print $page->li({class=>"logout"},
                                    $page->a({tabindex=>"4",accesskey=>"o",href=>"logout.cgi"},
                                             '<span xml:lang="en">Logout</span>')
                                 );      
                     }  
print $page->end_ul;
print $page->end_div;
}
sub footer($)
{
my $page=shift;
print $page->div({id=>"footer"},
                  "\n",
                  $page->p({id=>"authors"},
                           "Sito realizzato da G. Cattelan, A. Cornaglia, R. De Stefani, J. Sotomayor"
                           ),
                  "\n",
                  $page->ul({id=>"validation"},
                           $page->li(
                                    $page->a({href=>"http://validator.w3.org/check?uri=referer"},
                                             $page->span({lang=>en},
                                                         "Valid XHTML 1.0 Strict!"
                                                         )
                                             )
                                    ),
                           "\n",
                           $page->li(
                                    $page->a({href=>"http://jigsaw.w3.org/css-validator/check/referer"},
                                             $page->span({lang=>en},
                                                         "Valid CSS3!"
                                                         )
                                             )
                                    ),
                           "\n",
                           $page->li(
                                    $page->a({href=>"http://contentquality.com"},
                                             $page->span({lang=>en},
                                                         "Valid WCAG"
                                                         )
                                             )
                                    )
                           ),
                  $page->div({class=>"clear"},"")
                  );
}
1;
