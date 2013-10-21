
init=function(app){

}
name="Base64";
description="";
convert=function(toConvert){
	log.log(toConvert);
	var s = "<code class='prettyprint'>" + utils.atob(toConvert) + "</code>"; 
    return s;
}
