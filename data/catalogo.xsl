<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:v="http://www.monti.it">
<xsl:output method='html' version='1.0' encoding='UTF-8' indent='yes'
doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"
doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN"/>
<xsl:template match="/">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta name="language" content="it" />
		<meta name="author" content="Giacomo Cattelan, Alessandro Cornaglia, Riccardo De Stefani, Jorge Sotomayor" />
		<meta name="description" content=".." />
		<meta name="keywords" content=".." />
		<link href="screen.css" rel="stylesheet" media="screen" type="text/css" />
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
			Ti trovi in: <span xml:lang="en">Homepage</span>  Catalogo Vini
		</div>  <!--path-->
		<div id="container">
			<div id="navigation">
				<ul>
					<li class="homepage"> <a tabindex="1" accesskey="h" href="index.html"><span xml:lang="en">Homepage</span></a> </li>
					<li class="catalogo" id="here">Catalogo Vini</li>
					<li class="chisiamo"> <a tabindex="2" accesskey="s" href="chi_siamo.html">Chi Siamo</a> </li>
					<li class="contatti"> <a tabindex="3" accesskey="o" href="contatti.html">Contatti</a> </li>
					<li class="registrati"> <a tabindex="4" accesskey="r" href="registrati.html">Registrati</a> </li>
					<li class="login"> <a tabindex="5" accesskey="l" href="login.html"><span xml:lang="en">Login</span></a> </li>
				</ul>
			</div>  <!--navigation-->
			<div id="content">
                  
				<h2><a name="top"></a>Catalogo dei nostri prodotti</h2>
            <xsl:for-each select="v:data/v:prodotti/v:vino">
            	<xsl:sort select="v:etichetta"/>
               <div class="product_container">
                  <h3><xsl:value-of select="v:etichetta"/></h3>
                  <img src="" alt="" />
                  <div>
                     <dl>
                        <dt>Categoria:</dt>
                           <dd><xsl:value-of select="v:categoria"/></dd>
                        <dt>Stato:</dt>
                           <dd><xsl:value-of select="v:stato"/></dd>
                        <dt>Colore:</dt>
                           <dd><xsl:value-of select="v:colore"/></dd>
                     </dl>
                     <a href="visualizza_prodotto.html?vino=fiordarancio">Vedi tutte le caratteristiche</a>
                  </div>
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
