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
		<meta name="description" content="Cantina Benato, premiata cantina dal 1960, propone un catalogo dei propri vini tipici dei Colli Euganei. Registratevi al sito e potrete godere del beneficio di prenotare le vostre bottiglie preferite" />
		<meta name="keywords" content="cantina Benato, cantina, Benato, vini, vini bianchi, vini rossi, vini rosati, Colli Euganei, bottiglie, prenotazione" />
		<title>Homepage ~ Cantina Benato</title>
		<link href="../css/screen/main.css" rel="stylesheet" media="screen" type="text/css" />
		<link href="../css/print/main.css" rel="stylesheet" media="print" type="text/css" />
	</head>
	
	<body>
		<div id="header">
			<img src="../images/logo.png" width="260px" alt="" />
			<h1>Cantina Benato</h1>
			<p>Premiata cantina di Benato Romeo e figlio, dal 1960</p>
			<div class="clear"></div>
		</div>  <!--header -->
		<div id="path">
			Ti trovi in:
			<span xml:lang="en">Homepage</span>
		</div>  <!--path -->
		<div id="container">
			<a class="nav_help" href="#content"></a>
			<div id="navigation">
				<ul>
					<li class="homepage" id="here">
							<span xml:lang="en">Homepage</span>
					</li>
					<li class="catalogo">
						<a tabindex="1" accesskey="c" href="catalogo.cgi">Catalogo Vini<span class="acckey">(c)</span></a>
					</li>
					<li class="chisiamo">
						<a tabindex="2" accesskey="s" href="chi_siamo.cgi">Chi Siamo<span class="acckey">(s)</span></a>
					</li>
					<li class="areapersonale">
						<a tabindex="3" accesskey="a" href="areapersonale.cgi">Area Personale<span class="acckey">(a)</span></a>
					</li>
					<li class="logout">
						<a tabindex="4" accesskey="l" href="logout.cgi">
							<span xml:lang="en">Logout</span><span class="acckey">(l)</span>
						</a>
					</li>
				</ul>
			</div>  <!--navigation -->
			<div id="content">
				<h2>
					<a name="top"></a>
					I vini consigliati dalla nostra cantina
				</h2>
	
				<xsl:for-each select="v:dati/v:prodotti/v:vino[position()&lt;4]">
					<xsl:sort select="v:etichetta" />
						<div class="pr_container">
							<div class="pr_head">
								<h3>
									<xsl:value-of select="v:etichetta" />
								</h3>
							</div>
							<xsl:element name="img">
								<xsl:attribute name="src"><xsl:value-of
									select="v:immagine" /></xsl:attribute>
								<xsl:attribute name="alt">Bottiglia di <xsl:value-of select="v:etichetta"/></xsl:attribute>
								<xsl:attribute name="width">135px</xsl:attribute>
							</xsl:element>
							<div class="pr_body">
								<dl>
									<dt>Etichetta:</dt>
									<dd>
										<xsl:value-of select="v:etichetta" />
									</dd>
									<dt>Tipologia:</dt>
									<dd>
										Vino <xsl:value-of select="v:tipologia" />
									</dd>
									<dt>Categoria:</dt>
									<dd>
										Vino <xsl:value-of select="v:categoria" />
									</dd>
									<dt>Stato:</dt>
									<dd>
										Vino <xsl:value-of select="v:stato" />
									</dd>
									<dt>Prezzo unitario:</dt>
									<dd>
										Euro <xsl:value-of select="v:prezzo" />
									</dd>
								</dl>
							</div>
							<div class="clear"></div>
						</div> <!--product container -->
						
						<a class="internal_nav" href="#top">Torna su &#9650;</a>
	
				</xsl:for-each>
			</div>  <!--content -->
		</div>  <!--container-->
		<div id="footer">
			<p id="authors">
				Sito realizzato da G. Cattelan, A. Cornaglia, R. De Stefani, J.
				Sotomayor
			</p>
			<ul id="validation">
				<li>
					<a href="http://validator.w3.org/check?uri=referer">
						<span xml:lang="en">Valid XHTML 1.0 Strict!</span>
					</a>
				</li>
				<li>
					<a href="http://jigsaw.w3.org/css-validator/check/referer">
						<span xml:lang="en">Valid CSS3!</span>
					</a>
				</li>
				<li>
					<a href="http://contentquality.com">
						<span xml:lang="en">Valid WCAG Priority 2!</span>
					</a>
				</li>
			</ul>
			<div class="clear"></div>
		</div>  <!--footer -->
		</body>
	</html>
</xsl:template>
</xsl:stylesheet>
