#!/usr/bin/perl -w
use XML::LibXML;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use strict;

print "Content-type: text/html\n\n";

#creo oggetto CGI
my $pagina = new CGI;

#recupero dato se ricevuto o no;
my $spedito = $pagina->param('spedito');
my $prima_volta = 1;  #valore di default 
if ( $spedito == 1){  #se ho ricevuto i dati porto prima volta a 0
    $prima_volta = 0;
}

if ($prima_volta == 1){
#stampo html per richiedere i dati
  print '
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta name="language" content="it" />
		<meta name="author" content="Giacomo Cattelan, Alessandro Cornaglia, Riccardo De Stefani, Jorge Sotomayor" />
		<meta name="description" content=".." />
		<meta name="keywords" content=".." />
		<link href="css/screen/main.css" rel="stylesheet" media="screen" type="text/css" />
		<link href="css/print/main.css" rel="stylesheet" media="print" type="text/css" />
		<title>Homepage ~ Cantina Benato</title>
	</head>
	
	<body>
		<div id="header">
			<img src="images/logo.png" width="260px" alt="" />
			<h1>Cantina Benato</h1>
			<p>Premiata cantina di Benato Romeo e figlio, dal 1960</p>
			<div class="clear"></div>
		</div>  <!--header-->
		<div id="path">
			Ti trovi in: <span xml:lang="en">Homepage</span> &#187; Login
		</div>  <!--path-->
		<div id="container">
			<a class="nav_help" href="#content"></a>
			<div id="navigation">
				<ul>
					<li class="homepage"> <a tabindex="1" accesskey="h" href="index.html"><span xml:lang="en">Homepage</span></a> </li>
					<li class="catalogo"> <a tabindex="2" accesskey="c" href="catalogo.html">Catalogo Vini</a> </li>
					<li class="chisiamo"> <a tabindex="3" accesskey="s" href="chi_siamo.html">Chi Siamo</a> </li>
					<li class="registrati"> <a tabindex="4" accesskey="r" href="registrati.html">Registrati</a> </li>
					<li class="login" id="here"> <span xml:lang="en">Login</span> </li>
				</ul>
			</div>  <!--navigation-->
			<div id="content">
				<h2>Login al sito</h2>
				<form id="user" method="post" action="login.cgi">
					<fieldset>
						<legend>I tuoi dati d&apos;accesso</legend>
						<p>
							<label for="username">Il tuo username</label> 
							<input id="username" type="text" name="username" size="30" /> 
						</p>
						<p>
							<label for="password">La tua password</label>
							<input id="password" type="password" name="password" size="30" />
              <input id="spedito" name="spedito" type="hidden" value ="1" />
						</p>
					</fieldset>
					<p class="buttons">
						<input type="reset" value="Cancella" />
						<input type="submit" value="Entra" />
					</p>
				</form>									
			</div>  <!--content-->
		</div>  <!--container-->
		<div id="footer">
			<p id="authors">
				Sito realizzato da G. Cattelan, A. Cornaglia, R. De Stefani, J. Sotomayor
			</p>
			<ul id="validation">
				<li>
					<a href="http://validator.w3.org/check?uri=referer"><span xml:lang="en">Valid XHTML 1.0 Strict!</span></a>
				</li>
				<li>
					<a href="http://jigsaw.w3.org/css-validator/check/referer"><span xml:lang="en">Valid CSS3!</span></a>
				</li>
				<li>
					<a href="http://contentquality.com"><span xml:lang="en">Valid <acronym title="Web Content Accessibility Guidelines">WCAG</acronym> Priority 2!</span></a>
				</li>
			</ul>
			<div class="clear"></div>
		</div>  <!--footer-->
	</body>
</html>';
}  
else{
  my $username = $pagina->param('username');
  my $password = $pagina->param('password');
  my $chiave = "ciao";
  my $cryptPass = crypt($chiave,$password);
  
  #recupero i dati presenti nel database e li confronto con quelli inseriti
  if (&isPresente($username,$cryptPass) == 1){
    print "utente presente";
  }
  else{
    print "utente non presente"
  }
  
#devo effettuare i controlli
}

sub isPresente($){
  my $usr = shift;
  my $pass = shift;
  #vado a leggere il file xml
   my $db = "../data/db.xml";
   my $path ='//utente';
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
   
   my @usrs = $radice->findnodes($path);
   #my @username=$usrs[0]->getElementsByTagName('username');
   #my @supporto;
   my $lung = @usrs;
   #print $lung;
   for (my $i = 0; $i < $lung ; $i++){
     #my @elemento = $usrs[$i]->getElementsByTagName('username');
     my @elemento;
     push (@elemento,$usrs[$i]->getElementsByTagName('username'));
     push (@elemento,$usrs[$i]->getElementsByTagName('password'));
     my $i_usr = $elemento[0]->textContent;
     my $i_pass = $elemento[1]->textContent;  
     if (($i_usr eq $usr) && ($pass eq $i_pass)){
      return 1;
     }
   }
   return 0;
}
