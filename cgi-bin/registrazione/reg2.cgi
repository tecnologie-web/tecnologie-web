#!/usr/bin/perl -w
use XML::LibXML;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use strict;

print "Content-type: text/html\n\n";

#creo oggetto CGI
my $pagina = new CGI;

#controllo se ci sono dati nella sessione
  #recupero dati sessione
  my $username = $pagina->param('username');
  my $password = $pagina->param('password'); #non servono
  my $confirm_password = $pagina->param('confirm_password');
  my $nome = $pagina->param('nome');
  my $cognome = $pagina->param('cognome');
  my $email = $pagina->param('email');
  my $telefono = $pagina->param('telefono');
  #cripto password e confirm_password
  my $chiave = "ciao";
  my $cryptPass = crypt($chiave,$password);
  my $cryptControlPass = crypt($chiave,$confirm_password);
  #recupero dati errori
  my @err_usr;# = $pagina->param('err_usr');
  my @err_nome;# = $pagina->param('err_nome');
  my @err_cogn;# = $pagina->param('err_cogn');
  my @err_mail;# = $pagina->param('err_mail');
  my @err_tel;# = $pagina->param('err_tel');
  my @err_pass;
  #recupero dato se ricevuto o no;
  my $spedito = $pagina->param('spedito');
  #recupero numero errori
  #my $n_errori = @err_usr+@err_nome+@err_cogn+@err_mail+@err_tel;
  
  my $prima_volta = 1;  #valore di default 
  if ( $spedito == 1){  #se ho ricevuto i dati porto prima volta a 0
      $prima_volta = 0;
  }  
  
  #se è la prima volta che viene visualizzata la pagina allora la mostro vuota
  if ( $prima_volta == 1){
      print(&stampa_intera);
  }
  else{
   #devo effettuare i vari controlli
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
    
    
  if ($num_err == 0){print "DATI CORRETTI";
    #definisco file xml
    my $file = 'db.xml';

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
       <password>$password</password>
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
    my $fileDestinazione = "db.xml";
    open(OUT, ">$fileDestinazione") or die("Non riesco ad aprire il file in scrittura");
    #scrivo effettivamente sul file
    print OUT $doc->toString;
    #chiudo file
    close (OUT);

    #redirect
  }
  #se num_err == 0 allora vado alla pagina successiva
  else{  
    print (&stampa_prima);
    
    print ('<div id="content">
				<h2>Form di registrazione al sitowertyuiosdfghj</h2>	
				<form id="user" method="post" action="reg2.cgi" onsubmit="return registration();">
					<fieldset id="site">
						<legend>Dati accesso al sito</legend>
						<p>
							<label for="username">Scegli lo username</label> 
							<input id="username" type="text" name="username" size="30" value="'.$username.'"/>
              <input name="spedito" type="hidden" value="1" />
							<span class="help">'.&get_errore(@err_usr[0]).'</span>
						</p>
						<p>
							<label for="password">Scegli la password</label>
							<input id="password" type="password" name="password" size="30" />
							<span class="help">'.&get_errore(@err_pass[0]).'</span>
						</p>
						<p>
							<label for="confirm_password">Conferma la password</label>
							<input id="confirm_password" type="password" name="confirm_password" size="30" />
							<span class="help"></span>
						</p>
					</fieldset>
					<fieldset id="personal">
						<legend>Dati personali</legend>
						<p>
							<label for="nome">Il tuo nome</label>
							<input id="nome" type="text" name="nome" size="30" value="'.$nome.'"/>
							<span class="help">'.&get_errore(@err_nome[0]).'</span>
						</p>
						<p>
							<label for="cognome">Il tuo cognome</label>
							<input id="cognome" type="text" name="cognome" size="30" value="'.$cognome.'"/>
							<span class="help">'.&get_errore(@err_cogn[0]).'</span>
						</p>
						<p>
							<label for="email">La tua <span xml:lang="en">email</span></label>
							<input id="email" type="text" name="email" size="30" value="'.$email.'"/>
							<span class="help">'.&get_errore(@err_mail[0]).'</span>
						</p>
						<p>
							<label for="telefono">Il tuo telefono</label>
							<input id="telefono" type="text" name="telefono" size="30" value="'.$telefono.'"/>
							<span class="help">'.&get_errore(@err_tel[0]).'</span>
						</p>
					</fieldset>');
      print (&stampa_ultima);
    }
  #altrimenti rivisualizzo la pagina con gli errori riscontrati
  }#fine ramo se vista = 1

  #funzione che dato in ingresso un codice di errore restituisce una descrizione di esso
  sub get_errore($){
      ###############################
      #    TIPI DI ERRORE           #
      # 1 : campo contiene < o >    #
      # 2 : campo contiene char non #
      #     validi o numeri         #
      # 3 : campo non nel formato   #
      #     starndard               #
      # 4 : password e conferma non #
      #     corrispondono           #
      # 5 : già presente            #
      # 6 : campo vuoto             #
      ###############################
      my $errore = shift;
      if ($errore == 1){
        return "il campo non deve contenere < o >";
      }
      if ($errore == 2){
        return "il campo dati contiene caratteri non validi";
      }
      if ($errore == 3){
        return "il campo dati non è in forma standard";
      }
      if ($errore == 4){
        return "password e conferma non corrispondono";
      }
      if ($errore == 5){
        return "lo username è già presente";
      }
      if ($errore == 6){
        return "il campo non può essere lasciato vuoto";
      }
  }
  
  #funzione che cerca l'occorrenza di < o >
  sub angolari($){
    my $stringa = shift;
    #if ( $stringa =~ m/</ || $stringa =~ m/>/){
    if ($stringa =~ /^([\<]|[\>])$/){
      return 1;
    }
    else{
      if ( $stringa =~ /[\<\>]/) {
        return 1;
      }
      else{
      return 0;
      }
    }
  }
#fine angolari

#funzione che controlla se il campo è vuoto
sub not_vuoto($){
  my $stringa = shift;
  if( $stringa =~ /^$/){#se la stringa è così composta ok
    return 1;
  }
  else{#se non lo è
    return 0;
  }
}

#fine vuoto
#funzione che restituisce 1 se trova occorenze di caratteri non alfabetici
sub not_alpha($){
  my $stringa = shift;
  if( $stringa =~ /^([A-Za-z]+)( [A-Za-z]+)*$/){#se la stringa è così composta ok
    return 0;
  }
  else{#se non lo è
    if ( $stringa =~ /^([A-Za-zèùàòé][ a-zA-Z'èùàòé]*)+$/){#se è nella forma xxx'xxx
      return 0;
    }
    else{
      return 1;
    }
  }
}
#fine non alfabetici

#funzione che controlla se username è in forma corretta
sub not_numbchar($){
    my $stringa = shift;
    if( $stringa =~ /^([A-Za-z\d]+)$/){#se la stringa è così composta ok
      return 0;
    }
    else{
      return 1;
    }
}
#fine controllo username

#funzione che restituisce 1 se la mail non è nel formato xxx@xxx.xxx
sub control_mail($){
    my $mail = shift;
    if ($mail =~/^([\w\-\+\.]+)\@([\w\-\+\.]+)\.([\w\-\+\.]+)$/){
      return 0;
    }
    else{
      if ($mail =~/^$/){#mail è opzionale quindi può essere vuoto
          return 0;
      }
      else{
        return 1;
      }
    }
}
#fine control email

#funzione che restituisce uno se la stringa non è composta da soli numeri
sub  control_numb($){
    my $numb = shift;
    if ($numb =~/^(\d)+$/){
      return 0;
    }
    else{
      return 1;
    }
} 
#fine numeri
#funzione che stampa la prima parte di html
  sub stampa_prima{
    my $stringa = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta name="language" content="it" />
		<meta name="author" content="Giacomo Cattelan, Alessandro Cornaglia, Riccardo De Stefani, Jorge Sotomayor" />
		<meta name="description" content=".." />
		<meta name="keywords" content=".." />
		<link href="css/screen/main.css" rel="stylesheet" media="screen" type="text/css" />
		<link href="css/print/main.css" rel="stylesheet" media="print" type="text/css" />
		<script type="text/javascript" src="filter_catalogo.js"></script>
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
			Ti trovi in: <span xml:lang="en">Homepage</span> &#187; Registrati
		</div>  <!--path-->
		<div id="container">
			<a class="nav_help" href="#content">
			<div id="navigation">
				<ul>
					<li class="homepage"> <a tabindex="1" accesskey="c" href="index.html"><span xml:lang="en">Homepage</span></a> </li>
					<li class="catalogo"> <a tabindex="2" accesskey="c" href="catalogo.html">Catalogo Vini</a> </li>
					<li class="chisiamo"> <a tabindex="3" accesskey="s" href="chi_siamo.html">Chi Siamo</a> </li>
					<li class="registrati" id="here">Registrati</li>
					<li class="login"> <a tabindex="4" accesskey="l" href="login.html"><span xml:lang="en">Login</span></a> </li>
				</ul>
			</div>  <!--navigation-->';
            return $stringa;
  }
  
#funzione che stampa l'ultima parte di html
  sub stampa_ultima{
      return (
        '<p class="buttons">
						<input type="reset" value="Cancella" />
						<input type="submit" value="Invia"/>
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
</html>
');
  }

#funzione che stampa la pagina intera per la prima volta
sub stampa_intera{
  return ('
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
		<script type="text/javascript" src="filter_catalogo.js"></script>
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
			Ti trovi in: <span xml:lang="en">Homepage</span> &#187; Registrati
		</div>  <!--path-->
		<div id="container">
			<a class="nav_help" href="#content">
			<div id="navigation">
				<ul>
					<li class="homepage"> <a tabindex="1" accesskey="c" href="index.html"><span xml:lang="en">Homepage</span></a> </li>
					<li class="catalogo"> <a tabindex="2" accesskey="c" href="catalogo.html">Catalogo Vini</a> </li>
					<li class="chisiamo"> <a tabindex="3" accesskey="s" href="chi_siamo.html">Chi Siamo</a> </li>
					<li class="registrati" id="here">Registrati</li>
					<li class="login"> <a tabindex="4" accesskey="l" href="login.html"><span xml:lang="en">Login</span></a> </li>
				</ul>
			</div>  <!--navigation-->
			<div id="content">
				<h2>Form di registrazione al sito</h2>	
				<form id="user" method="post" action="reg2.cgi" onsubmit="return registration();>
					<fieldset id="site">
						<legend>Dati accesso al sito</legend>
						<p>
              <input name="spedito" type="hidden" value="1" />
							<label for="username">Scegli lo username</label> 
							<input id="username" type="text" name="username" size="30" />
              
							<span class="help"></span>
						</p>
						<p>
							<label for="password">Scegli la password</label>
							<input id="password" type="password" name="password" size="30" />
							<span class="help"></span>
						</p>
						<p>
							<label for="confirm_password">Conferma la password</label>
							<input id="confirm_password" type="password" name="confirm_password" size="30" />
							<span class="help"></span>
						</p>
					</fieldset>
					<fieldset id="personal">
						<legend>Dati personali</legend>
						<p>
							<label for="nome">Il tuo nome</label>
							<input id="nome" type="text" name="nome" size="30" />
							<span class="help"></span>
						</p>
						<p>
							<label for="cognome">Il tuo cognome</label>
							<input id="cognome" type="text" name="cognome" size="30" />
							<span class="help"></span>
						</p>
						<p>
							<label for="email">La tua <span xml:lang="en">email</span></label>
							<input id="email" type="text" name="email" size="30" />
							<span class="help"></span>
						</p>
						<p>
							<label for="telefono">Il tuo telefono</label>
							<input id="telefono" type="text" name="telefono" size="30" />
							<span class="help"></span>
						</p>
					</fieldset>
					<p class="buttons">
						<input type="reset" value="Cancella" />
						<input type="submit" value="Invia"/>
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
</html>');
  
}

#funzione che controlla se lo username passato è presente nel db
sub isPresente($){
  my $usr = shift;
  
  #vado a leggere il file xml
   my $db = "db.xml";
   my $path ='//utente';#vino[etichetta="'.$input{vino}.'"]';
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
   my @username=$usrs[0]->getElementsByTagName('username');
   my @supporto;
   my $lung = @usrs;
   #print $lung;
   for (my $i = 0; $i < $lung ; $i++){
     my @elemento = $usrs[$i]->getElementsByTagName('username');
     my $zio = $elemento[0]->textContent;
     if ($zio eq $usr){
      return 1;
     }
   }
   return 0;
}
