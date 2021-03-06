<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:v="http://www.cantinabenato.it">
	<xsl:output method='html' version='1.0' encoding='UTF-8'
		doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"
		doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" indent='yes' />
	<xsl:template match="/">
		<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
			<head>
				<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
				<meta name="language" content="it" />
				<meta name="author"
					content="Giacomo Cattelan, Alessandro Cornaglia, Riccardo De Stefani, Jorge Sotomayor" />
				<meta name="description"
					content="Cantina Benato, vendita al dettaglio presso la nostra cantina di Boccon di Vo e prenotazione dal nostro catalogo online di vini tipici dei Colli Euganei in bottiglia " />
				<meta name="keywords"
					content="Cantina Benato, catalogo, vini in bottiglia, vini bianchi, vini rossi, vini rosati, vini dolci, vini secchi, vini frizzanti, vini fermi, vini spumanti" />
				<link href="../css/screen/main.css" rel="stylesheet" media="screen"
					type="text/css" />
				<link href="../css/print/main.css" rel="stylesheet" media="print"
					type="text/css" />
				<title>Catalogo Vini ~ Cantina Benato</title>
				<script src="../js/scripts.js" type="text/javascript"></script>
			</head>

			<body onload="focusOnSearchEtichetta();">
				<div id="header">
					<img src="../images/logo.png" width="260px" alt="" />
					<h1>Cantina Benato</h1>
					<p>Premiata cantina di Benato Romeo e figlio, dal 1960</p>
					<div class="clear"></div>
				</div>  <!--header -->
				<div id="path">
					Ti trovi in:
					<span xml:lang="en">Homepage</span>
					&#187; Catalogo Vini
				</div>  <!--path -->
				<div id="container">
					<a class="nav_help" href="#content"></a>
					<div id="navigation">
						<ul>
							<li class="homepage">
								<a tabindex="1" accesskey="h" href="index.cgi">
									<span xml:lang="en">Homepage</span><span class="acckey">(h)</span>
								</a>
							</li>
							<li class="catalogo" id="here">Catalogo Vini</li>
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
							Catalogo dei nostri prodotti
						</h2>

						<form id="search" action="#" onsubmit="return false;">
							<fieldset>
								<legend>Ricerca Vini</legend>
								<p>
									<label id="etich" for="etichetta">per etichetta:</label>
									<span>
										<input name="etichetta" id="etichetta" type="text" size="30"
											onchange="filter();" />
									</span>
									<span id="hint">Digita il nome del vino (o parte di esso) che desideri cercare e premi INVIO</span>
								</p>
								<p>
									<label>per tipologia:</label>
									<span>
										<label class="check" for="bianchi">Vini Bianchi</label>
										<input type="checkbox" id="bianchi" name="bianchi"
											value="Vino Bianco" checked="checked" onclick="filter();" />
										<label class="check" for="rossi">Vini Rossi</label>
										<input type="checkbox" id="rossi" name="rossi" value="Vino Rosso"
											checked="checked" onclick="filter();" />
										<label class="check" for="rosati">Vini Rosati</label>
										<input type="checkbox" id="rosati" name="rosati" value="Vino Rosato"
											checked="checked" onclick="filter();" />
									</span>
								</p>
								<p>
									<label>per categoria:</label>
									<span>
										<label class="check" for="secchi">Vini Secchi</label>
										<input type="checkbox" id="secchi" name="secchi" value="Vino Secco"
											checked="checked" onclick="filter()" />
										<label class="check" for="dolci">Vini Dolci</label>
										<input type="checkbox" id="dolci" name="dolci" value="Vino Dolce"
											checked="checked" onclick="filter()" />
									</span>
								</p>
								<p>
									<label>per stato:</label>
									<span>
										<label class="check" for="frizzanti">Vini Frizzanti</label>
										<input type="checkbox" id="frizzanti" name="frizzanti"
											value="Vino Frizzante" checked="checked" onclick="filter()" />
										<label class="check" for="fermi">Vini Fermi</label>
										<input type="checkbox" id="fermi" name="fermi" value="Vino Fermo"
											checked="checked" onclick="filter()" />
										<label class="check" for="spumanti">Vini Spumanti</label>
										<input type="checkbox" id="spumanti" name="spumanti"
											value="Vino Spumante" checked="checked" onclick="filter()" />
									</span>
								</p>
							</fieldset>
						</form>
						<xsl:for-each select="v:dati/v:prodotti/v:vino">
							<xsl:sort select="v:etichetta" />
							<div class="pr_container_wrapper">
								<div class="pr_container">
									<div class="pr_head">
										<h3>
											<xsl:element name="a">
												<xsl:attribute name="name">v<xsl:value-of select="position()" /></xsl:attribute>
											</xsl:element>
											<xsl:value-of select="v:etichetta" />
										</h3>
										<form class="form_prenota" method="post" action="prenota.cgi">
											<fieldset>
												<xsl:element name="input">
													<xsl:attribute name="type">hidden</xsl:attribute>
													<xsl:attribute name="name">posizione</xsl:attribute>
													<xsl:attribute name="value">v<xsl:value-of select="position()"/></xsl:attribute>
												</xsl:element>
												<xsl:element name="input">
													<xsl:attribute name="type">hidden</xsl:attribute>
													<xsl:attribute name="name">etichetta</xsl:attribute>
													<xsl:attribute name="value"><xsl:value-of
														select="v:etichetta" /></xsl:attribute>
												</xsl:element>
												<xsl:element name="label">
													<xsl:attribute name="for">l<xsl:value-of select="position()" /></xsl:attribute>Quantità
												</xsl:element>
												<xsl:element name="input">
													<xsl:attribute name="type">text</xsl:attribute>
													<xsl:attribute name="id">l<xsl:value-of select="position()" /></xsl:attribute>
													<xsl:attribute name="name">quantita</xsl:attribute>
													<xsl:attribute name="value"></xsl:attribute>
													<xsl:attribute name="size">1</xsl:attribute>
												</xsl:element>

												<input class="prenota" type="submit" value="Prenota" />
											</fieldset>
										</form>
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
										<xsl:element name="a">
											<xsl:attribute name="href">visualizza_prodotto.cgi?vino=<xsl:value-of
												select="v:etichetta" /></xsl:attribute>
											Vedi tutte le caratteristiche
										</xsl:element>
									</div>
									<div class="clear"></div>

								</div> <!--product container -->
								<a class="internal_nav" href="#top">Torna su &#9650;</a>
							</div>
						</xsl:for-each>
					</div>  <!--content -->
				</div>  <!--container -->
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
