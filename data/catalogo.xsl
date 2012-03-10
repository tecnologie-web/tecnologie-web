<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:v="http://www.cantinabenato.it">
<xsl:output method='html' version='1.0' encoding='UTF-8' 
doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"
doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN"
indent='yes'/>
<xsl:template match="/">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta name="language" content="it" />
		<meta name="author" content="Giacomo Cattelan, Alessandro Cornaglia, Riccardo De Stefani, Jorge Sotomayor" />
		<meta name="description" content=".." />
		<meta name="keywords" content=".." />
		<link href="../css/screen/main.css" rel="stylesheet" media="screen" type="text/css" />
		<link href="../css/print/main.css" rel="stylesheet" media="print" type="text/css" />
		<title>Catalogo Vini ~ Cantina Benato</title>
	</head>
	
	<body>
		<div id="header">
			<img src="images/logo.png" width="260px" alt="" />
			<h1>Cantina Benato</h1>
			<p>Premiata cantina di Benato Romeo e figlio, dal 1960</p>
			<div class="clear"></div>
		</div>  <!--header-->
		<div id="path">
			Ti trovi in: <span xml:lang="en">Homepage</span> &#187; Catalogo Vini
		</div>  <!--path-->
		<div id="container">
			<div id="navigation">
				<ul>
					<li class="homepage"> <a tabindex="1" accesskey="h" href="index.html"><span xml:lang="en">Homepage</span></a> </li>
					<li class="catalogo" id="here">Catalogo Vini</li>
					<li class="chisiamo"> <a tabindex="2" accesskey="s" href="chi_siamo.html">Chi Siamo</a> </li>
					<li class="registrati"> <a tabindex="3" accesskey="r" href="registrati.html">Registrati</a> </li>
					<li class="login"> <a tabindex="4" accesskey="l" href="login.html"><span xml:lang="en">Login</span></a> </li>
				</ul>
			</div>  <!--navigation-->
			<div id="content">
				<h2><a name="top"></a>Catalogo dei nostri prodotti</h2>
				
					<form id="search">
						<fieldset>
						<legend>Ricerca Vini</legend>
						<p>
							<label id="etich" for="etichetta">per etichetta:</label>
							<span>
								<input name="etichetta" id="etichetta" type="text" size="30" />
							</span>
						</p>
						<p>
							<label>per tipologia:</label>
							<span>
								<label class="check" for="bianchi">Vini Bianchi</label>
								<input type="checkbox" id="bianchi" name="bianchi" value="bianchi" checked="true" />
								<label class="check" for="rossi">Vini Rossi</label>
								<input type="checkbox" id="rossi" name="rossi" value="rossi" checked="true" />
								<label class="check" for="rosati">Vini Rosati</label>
								<input type="checkbox" id="rosati" name="rosati" value="rosati" checked="true" />
							</span>
						</p>
						<p>
							<label>per categoria:</label>
							<span>
								<label class="check" for="dolci">Vini Dolci</label>
								<input type="checkbox" id="dolci" name="dolci" value="dolci" checked="true" />
								<label class="check" for="secchi">Vini Secchi</label>
								<input type="checkbox" id="secchi" name="secchi" value="secchi" checked="true" />
							</span>
						</p>
						<p>
							<label>per stato:</label>
							<span>
								<label class="check" for="frizzanti">Vini Frizzanti</label>
								<input type="checkbox" id="frizzanti" name="frizzanti" value="frizzanti" checked="true" />
								<label class="check" for="fermi">Vini Fermi</label>
								<input type="checkbox" id="fermi" name="fermi" value="fermi" checked="true" />
								<label class="check" for="spumanti">Vini Spumanti</label>
								<input type="checkbox" id="spumanti" name="spumanti" value="spumanti" checked="true" />
							</span>
						</p>
						</fieldset>
					</form>
               <xsl:for-each select="v:dati/v:prodotti/v:vino">
                  <xsl:sort select="v:etichetta"/>
						<div class="pr_container">
                  <div id="pr_head">
						<h3>Fior d'arancio</h3>
						<form id="form_prenota" method="post" action="cgi-bin/prenota.cgi">
							<fieldset>
								<input type="hidden" name="etichetta" value=''/>
                        <xsl:attribute-set name="input">
                           <xsl:attribute name="type">hidden</xsl:attribute>
                           <xsl:attribute name="name">etichetta</xsl:attribute>
                           <xsl:attribute name="value"><xsl:value-of select="v:etichetta"/></xsl:attribute>
                        </xsl:attribute-set>
								<label for="quantita">Quantità</label>
								<input type="text" name="quantita" value="6" size="1" />
								<input id="prenota" type="submit" value="Prenota" />
							</fieldset>
						</form>
					</div>
					<img src="images/prodotti/fiordarancio.png" alt="" />
					<dl>
						<dt>Etichetta:</dt>
							<dd><xsl:value-of select="v:etichetta"/></dd>
						<dt>Tipologia:</dt>
							<dd><xsl:value-of select="v:tipologia"/></dd>
						<dt>Categoria:</dt>
							<dd>Vino <xsl:value-of select="v:categoria"/></dd>
						<dt>Stato:</dt>
							<dd>Vino <xsl:value-of select="v:stato"/></dd>
						<dt>Prezzo:</dt>
							<dd><xsl:value-of select="@valuta"/> <xsl:value-of select="v:prezzo"/></dd>
					</dl>
					<a href="visualizza_prodotto.html?vino=barbera">Vedi tutte le caratteristiche</a>
               </div> <!--product container-->
               </xsl:for-each> 
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
</xsl:template>
</xsl:stylesheet>
