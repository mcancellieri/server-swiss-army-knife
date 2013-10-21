
init=function(app){

}
name="JSON";
description="";
convert=function(toConvert){
	log.log(toConvert);
	var s = "<code class='prettyprint'>" + utils.htmlencoder.htmlEncode(utils.prettydata.json(toConvert, 4 )) + "</code>"; 
    return s;
}
