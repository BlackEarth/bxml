<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="2.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:a="http://relaxng.org/ns/compatibility/annotations/1.0" 
    xmlns:sch="http://purl.oclc.org/dsdl/schematron"
    xmlns:rng="http://relaxng.org/ns/structure/1.0"
    xmlns="http://www.w3.org/1999/xhtml">

    <xsl:output method="text" encoding="utf-8" indent="no"/>

    <xsl:param name="schema_version"/>

    <xsl:template match="/">
        <xsl:apply-templates select="//a:documentation | //rng:define | //sch:rule "/>
    </xsl:template>

    <xsl:template match="*|comment()"/>

    <xsl:template match="a:documentation">
        <xsl:text>&#xA;&#xA;</xsl:text> 
        <xsl:value-of select="text()"/>
    </xsl:template>

    <xsl:template match="rng:define">
        <xsl:text>&#xA;&#xA;## </xsl:text>
        <xsl:value-of select="@name"></xsl:value-of>
    </xsl:template>

    <xsl:template match="sch:rule">
        <xsl:if test="@title">
            <xsl:text>&#xA;&#xA;### Rule: </xsl:text>
            <xsl:value-of select="@title"/>
        </xsl:if>
        <xsl:text>&#xA;`</xsl:text>
        <xsl:value-of select="@context"></xsl:value-of>
        <xsl:text>`&#xA;{: .code}</xsl:text>
        <xsl:for-each select="sch:assert">
            <xsl:text>&#xA;&#xA;* </xsl:text>
            <xsl:value-of select="."/>
            <xsl:text>&#xA;&#xA;    `</xsl:text>
            <xsl:value-of select="@test"/>
            <xsl:text>`&#xA;    {: .code}</xsl:text>
        </xsl:for-each>
    </xsl:template>

</xsl:stylesheet>