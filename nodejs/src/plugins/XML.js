
init=function(app){

}
name="XML";
description="";
convert=function(toConvert){
	log.log(toConvert);
	var s = "<code class='prettyprint'>" + utils.htmlencoder.htmlEncode(utils.prettydata.xml(toConvert, 4 )) + "</code>"; 
    return s;
}
