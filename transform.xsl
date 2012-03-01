<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:v="http://www.monti.it" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method='html' version='1.0' encoding='UTF-8' indent='yes'/>
<xsl:template match="/">
<html>
	<head>
		<title>Vini</title>
	</head>
	<body>
		<h3>Elenco nomi vini</h3>
		<ul>
			<xsl:for-each select="v:data/v:prodotti/v:vino">
				<li> <xsl:value-of select="v:etichetta"/> </li>
			</xsl:for-each>
		</ul>
	</body>
</html>
</xsl:template>
</xsl:stylesheet>