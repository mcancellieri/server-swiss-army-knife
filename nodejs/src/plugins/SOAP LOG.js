
init=function(app){

}
name="SOAPLOG";
description="";
convert=function(toConvert){
	
	var purged = toConvert.replace(/^.* SOAP (REQUEST|RESPONSE) \d+\/\d+:\s/gim,'');
	purged = purged.replace(/correlationId=.*,.*$/gim,'');
	var s = "<code class='prettyprint'>" + utils.htmlencoder.htmlEncode(utils.prettydata.xml(purged, 4 )) + "</code>"; 
    return s;
}
