#!/usr/bin/perl
sub togli_ns($){
   my $db = shift;
   my $file_content = "";
   open(INPUT,$db);
   while(<INPUT>) 
   {
      $file_content = $file_content.$_;
   }
   $file_content =~ s/<dati .+>(.*)<iscritti>/<dati>\1<iscritti>/s;
   return $file_content;
}
1;
