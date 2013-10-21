function htmlEncode(value){
    if (value) {
        return jQuery('<div />').text(value).html();
    } else {
        return '';
    }
}
 
function htmlDecode(value) {
    if (value) {
        return $('<div />').html(value).text();
    } else {
        return '';
    }
}
function cleanText(text){
    text = text.replace("\\n","")
    text = text.replace("\\","")
	return text;
}

function toggleCollapse(elem){
	if ($("#" + elem).hasClass('visibleDiv')){
		$("#" + elem).removeClass('visibleDiv');
		$("#" + elem).addClass('collapsedDiv');
	} else if ($("#" + elem).hasClass('collapsedDiv')){
		$("#" + elem).removeClass('collapsedDiv');
		$("#" + elem).addClass('visibleDiv');
	}
}