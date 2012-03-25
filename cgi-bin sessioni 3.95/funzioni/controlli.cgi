#!/usr/bin/perl

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
#fine get_errore()

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
#fine not_vuoto

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
#fine not_alpha

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
#fine not_numbchar

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
#fine control_mail

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
#fine control_numb

#funzione che controlla se lo username passato è presente nel db
  sub isPresente($){
    my $usr = shift;
    
    #vado a leggere il file xml
     my $db = "../data/db.xml";
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
       my $el = $elemento[0]->textContent;
       if ($el eq $usr){
        return 1;
       }
     }
     return 0;
  }
#fine isPresente
1;
